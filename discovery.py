#!/usr/bin/env python3
"""Discovery engine: ARP sweep + PROFINET DCP + EtherNet/IP CIP, con classificazione tipo device."""

import ipaddress
import logging
import socket
import subprocess
import sys

import psutil
import hostname
from mac_vendors_db import MAC_VENDORS
from pnio_dcp import DCP
from pycomm3 import CIPDriver
from scapy.all import arping, getmacbyip

log = logging.getLogger("ot.discovery")

PROTO_PRIORITY = {"ARP": 1, "CIP": 2, "PROFINET": 3}


def lookup_vendor(mac):
    if not mac:
        return ""
    oui = str(mac).replace(":", "").replace("-", "").replace(".", "").upper()[:6]
    return MAC_VENDORS.get(oui, "")


def resolve_interfaces(iface_cfg):
    """Restituisce la lista {name, ip, netmask} delle interfacce di scoperta.
    iface_cfg: stringa separata da virgola (nome, IP o 'auto').
    'auto' -> tutte le NIC IPv4 (escluso loopback)."""
    nets = []
    for name, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                nets.append({"name": name, "ip": addr.address, "netmask": addr.netmask})

    cfg = (iface_cfg or "auto").strip()

    if cfg.lower() == "auto":
        nets = [n for n in nets if not n["ip"].startswith("127.")]
        if not nets:
            raise RuntimeError("Interfaccia 'auto': nessuna NIC IPv4 trovata.")
        return nets

    resolved = []
    seen = set()
    for part in (p.strip() for p in cfg.split(",")):
        if not part or part in seen:
            continue
        seen.add(part)
        for n in nets:
            if part == n["ip"] or part.lower() == n["name"].lower():
                resolved.append(n)
                break
        else:
            raise RuntimeError(f"Interfaccia '{part}' non trovata. Disponibili: "
                               + ", ".join(f"{n['name']} ({n['ip']})" for n in nets))
    if not resolved:
        raise RuntimeError("Nessuna interfaccia specificata in line.iface / --iface.")
    return resolved


def ping(ip, timeout_sec=1):
    """Ping ICMP cross-platform (fallback stato per device noti che non rispondono ad ARP)."""
    if sys.platform == "win32":
        cmd = ["ping", "-n", "1", "-w", str(int(timeout_sec * 1000)), ip]
    else:
        cmd = ["ping", "-c", "1", "-W", str(int(timeout_sec)), ip]
    try:
        return subprocess.run(cmd, capture_output=True, timeout=timeout_sec + 2).returncode == 0
    except Exception:
        return False


def arp_scan(ip, netmask, iface_name, timeout_sec=2):
    """Sweep ARP della sottorete. Restituisce lista device 'ARP'."""
    results = []
    net = str(ipaddress.ip_network(f"{ip}/{netmask}", strict=False))
    try:
        ans, _ = arping(net, iface=iface_name, timeout=timeout_sec, verbose=0)
    except Exception as e:
        log.error("ARP scan fallito su %s (%s): %s", net, iface_name, e)
        return results

    for _, rcv in ans:
        mac = (rcv.hwsrc or "").lower()
        results.append({
            "protocol": "ARP",
            "ip": rcv.psrc,
            "name": "",
            "vendor": lookup_vendor(mac),
            "mac": mac,
            "product_type": "",
            "firmware": "",
            "serial": "",
        })
    return results


def discover_profinet(iface_ip, timeout_sec=5):
    """PROFINET DCP identify_all. Restituisce lista device 'PROFINET'."""
    results = []
    try:
        dcp = DCP(iface_ip)
        try:
            dcp.identify_all_timeout = timeout_sec
        except AttributeError:
            pass
        try:
            devices = dcp.identify_all(timeout=timeout_sec)
        except TypeError:
            devices = dcp.identify_all()
    except Exception as e:
        log.error("PROFINET DCP discovery fallita: %s", e)
        return results

    for dev in devices or []:
        mac = str(getattr(dev, "MAC", "") or "").lower()
        results.append({
            "protocol": "PROFINET",
            "ip": str(getattr(dev, "IP", "") or ""),
            "name": str(getattr(dev, "name_of_station", "") or ""),
            "vendor": lookup_vendor(mac),
            "mac": mac,
            "product_type": str(getattr(dev, "family", "") or ""),
            "firmware": "",
            "serial": "",
        })
        log.info("PROFINET: %s (%s)", results[-1]["ip"], results[-1]["name"])
    return results


def cip_port_open(ip, port=44818, timeout=0.5):
    """Verifica se la porta CIP (44818) e' raggiungibile via TCP."""
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except Exception:
        return False


def _parse_cip_identity(device, fallback_ip, mac_map):
    ip = str(device.get("ip_address") or fallback_ip or "")
    mac = str(device.get("MAC") or "")
    if not mac and ip:
        mac = (mac_map or {}).get(ip) or ""
    if not mac and ip:
        try:
            mac = str(getmacbyip(ip) or "")
        except Exception:
            mac = ""
    mac = mac.lower()

    rev = device.get("revision") or {}
    if isinstance(rev, dict):
        firmware = f"{rev.get('major', 0)}.{rev.get('minor', 0)}"
    else:
        firmware = str(rev)

    vendor = str(device.get("vendor") or "") or lookup_vendor(mac)

    return {
        "protocol": "CIP",
        "ip": ip,
        "name": str(device.get("product_name") or ""),
        "vendor": vendor,
        "mac": mac,
        "product_type": str(device.get("product_type") or ""),
        "firmware": firmware,
        "serial": str(device.get("serial") or ""),
    }


def scan_cip_ip(ip, port=44818, timeout=0.5, mac_map=None):
    """ListIdentity unicast verso un singolo ip (nessun broadcast).
    Pre-check TCP sulla porta 44818; restituisce lista device 'CIP'."""
    if not cip_port_open(ip, port, timeout):
        return []
    try:
        devices = CIPDriver.discover(ip)
    except Exception as e:
        log.warning("CIP discover(%s) fallita: %s", ip, e)
        return []

    results = []
    for device in devices or []:
        try:
            results.append(_parse_cip_identity(device, ip, mac_map))
            log.info("CIP: %s - %s", results[-1]["ip"], results[-1]["name"])
        except Exception as e:
            log.warning("CIP: errore parsing risposta %s: %s", device, e)
    return results


def discover_cip(candidate_ips, cfg, mac_map=None):
    """EtherNet/IP discovery per-indirizzo: porta 44818 aperta -> ListIdentity unicast.
    Niente broadcast 255.255.255.255 (linee senza router/broadcast device).
    candidate_ips: IP candidati (tipicamente quelli visti da ARP).
    Ritorna lista device 'CIP'."""
    results = []
    port = int(cfg["discovery"].get("cip_port", 44818))
    timeout = float(cfg["discovery"].get("cip_port_timeout", 0.5))

    ips = list(dict.fromkeys(ip for ip in candidate_ips if ip))
    extra = cfg["discovery"].get("cip_extra_ips") or []
    ips += [str(ip).strip() for ip in extra if str(ip).strip()]
    ips = list(dict.fromkeys(ips))

    if not ips:
        if cfg["discovery"].get("cip_broadcast_fallback", False):
            log.warning("CIP: nessun candidato, fallback broadcast")
            return discover_cip_broadcast()
        log.warning("CIP: nessun candidato IP (abilita discovery.arp o discovery.cip_extra_ips)")
        return results

    log.info("CIP: scan su %d IP candidati (porta %d)", len(ips), port)
    for ip in ips:
        results += scan_cip_ip(ip, port=port, timeout=timeout, mac_map=mac_map)
    log.info("CIP devices: %d", len(results))
    return results


def discover_cip_broadcast():
    """Vecchia modalita' ListIdentity broadcast (utile solo con router/broadcast)."""
    results = []
    try:
        devices = CIPDriver.discover()
    except Exception as e:
        log.error("CIP broadcast discovery fallita: %s", e)
        return results
    for device in devices or []:
        try:
            results.append(_parse_cip_identity(device, "", None))
            log.info("CIP: %s - %s", results[-1]["ip"], results[-1]["name"])
        except Exception as e:
            log.warning("CIP: errore parsing risposta %s: %s", device, e)
    return results


def merge_results(arp_devices, cip_devices, profinet_devices):
    """Merge per MAC (fallback IP). Priorita': PROFINET > CIP > ARP. Traccia seen_by."""
    devices = {}

    for dev in arp_devices:
        key = dev["mac"] or f"ip:{dev['ip']}"
        entry = {**dev, "seen_by": [dev["protocol"]]}
        devices[key] = entry

    for dev in cip_devices + profinet_devices:
        key = (dev.get("mac") or "").lower() or f"ip:{dev.get('ip', '')}"
        current = devices.get(key)
        if current is None:
            devices[key] = {**dev, "seen_by": [dev["protocol"]]}
            continue

        merged = {**current}
        for field, value in dev.items():
            if value:
                merged[field] = value
        seen = list(dict.fromkeys(current["seen_by"] + [dev["protocol"]]))
        if PROTO_PRIORITY[dev["protocol"]] > PROTO_PRIORITY[current["protocol"]]:
            merged["protocol"] = dev["protocol"]
        merged["seen_by"] = seen
        devices[key] = merged

    return list(devices.values())


def classify(device, pc_vendor_keywords):
    """allen_bradley | siemens | profinet | ethernetip | pc | generic."""
    seen = set(device.get("seen_by") or [device.get("protocol", "ARP")])
    vendor = (device.get("vendor") or "").lower()

    if "CIP" in seen and ("rockwell" in vendor or "allen" in vendor):
        return "allen_bradley"
    if "PROFINET" in seen:
        return "siemens" if "siemens" in vendor else "profinet"
    if "CIP" in seen:
        return "ethernetip"
    if any(k.lower() in vendor for k in pc_vendor_keywords):
        return "pc"
    return "generic"


def discover_all(ifaces, cfg):
    """Ciclo discovery completo. ifaces = lista {name, ip, netmask}.
    ARP e DCP su ogni interfaccia; CIP in modalita' per-indirizzo (port check
    + ListIdentity unicast) sui IP candidati visti da ARP/DCP.
    Restituisce lista device classificata (dedup per MAC/IP tra interfacce)."""
    arp_devices, cip_devices, profinet_devices = [], [], []

    if cfg["discovery"].get("arp", True):
        for iface in ifaces:
            found = arp_scan(iface["ip"], iface["netmask"], iface["name"])
            log.info("ARP devices su %s (%s): %d", iface["name"], iface["ip"], len(found))
            arp_devices += found

        # hostname iniziale dei device solo-ARP; nel merge restano solo se
        # DCP/CIP non forniscono name_of_station / product_name (precedenza)
        hostname.resolve_devices(arp_devices, cfg)

    if cfg["discovery"].get("dcp", True):
        timeout = int(cfg["discovery"].get("dcp_timeout_sec", 5))
        for iface in ifaces:
            found = discover_profinet(iface["ip"], timeout)
            log.info("PROFINET devices su %s (%s): %d", iface["name"], iface["ip"], len(found))
            profinet_devices += found

    if cfg["discovery"].get("cip", True):
        candidates = [d["ip"] for d in arp_devices + profinet_devices if d.get("ip")]
        mac_map = {d["ip"]: d["mac"] for d in arp_devices + profinet_devices
                   if d.get("ip") and d.get("mac")}
        cip_devices = discover_cip(candidates, cfg, mac_map)

    merged = merge_results(arp_devices, cip_devices, profinet_devices)
    keywords = cfg.get("pc_vendor_keywords") or []
    for dev in merged:
        dev["type"] = classify(dev, keywords)

    log.info("Device totali (dopo merge): %d", len(merged))
    return merged
