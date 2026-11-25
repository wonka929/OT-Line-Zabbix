#!/usr/bin/env python3
"""Risoluzione hostname device su LAN senza DNS: query unicast direct-to-device.

Metodi (in ordine):
1. NetBIOS node status (UDP 137, unicast) - replica di ping -a / impacket
   getnodestatus('*', ip): copre Windows (e Samba).
2. mDNS reverse (UDP 5353, unicast con bit QU) - PTR a.b.c.d.in-addr.arpa
   diretto al device: copre Avahi/Linux, macOS, IoT.
3. Resolver di sistema gethostbyaddr (opzionale, hostname_system).

Solo socket UDP standard: niente raw socket, niente root/Npcap per la
risoluzione. Parsing dei pacchetti con scapy in dissection offline.
"""

import logging
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.netbios import NBNSHeader, NBNSNodeStatusResponse

log = logging.getLogger("ot.hostname")

_NBNS_PORT = 137
_MDNS_PORT = 5353

# NBSTAT request wildcard: header (TXID=0, flags=0, QDCOUNT=1) +
# nome NetBIOS codificato "*" (length 0x20 + first-level encoding "CK"+"A"*30)
# + 0x00 + QTYPE=0x0021 (NBSTAT) + QCLASS=0x0001 (IN)
_NBSTAT_REQ = (
    b"\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00"
    b"\x20CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00"
    b"\x00\x21\x00\x01"
)

# cache positiva per processo: ip -> (hostname, ts)
_cache = {}
_CACHE_TTL = 3600


def _udp_query(req, ip, port, timeout):
    """Invio unicast UDP diretto a ip:port, ritorna i bytes della risposta."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout)
        sock.sendto(req, (ip, port))
        data, addr = sock.recvfrom(4096)
        if addr[0] != ip:
            return None
        return data


def get_netbios_name(ip, timeout=1.0):
    """NetBIOS node status (UDP 137, unicast): hostname Windows/Samba."""
    try:
        data = _udp_query(_NBSTAT_REQ, ip, _NBNS_PORT, timeout)
        if not data:
            return None
        pkt = NBNSHeader(data)
        resp = pkt.getlayer(NBNSNodeStatusResponse)
        if resp is None:
            # bind non matchato (flags atipici): prova dalla sezione answer.
            # Con question echo: 12 + (1+32+1+4) = 50; senza: 12.
            for offset in (50, 12):
                if len(data) <= offset:
                    continue
                try:
                    resp = NBNSNodeStatusResponse(data[offset:])
                    if resp.NODE_NAME:
                        break
                except Exception:
                    resp = None
        if resp is None:
            return None

        names = []
        for entry in resp.NODE_NAME or []:
            raw = entry.NETBIOS_NAME
            if isinstance(raw, bytes):
                raw = raw.decode("latin-1", "replace")
            raw = str(raw or "").strip("\x00 ").strip()
            if not raw:
                continue
            # SUFFIX 0x00 = workstation service (preferito), 0x20 = file server
            names.append((int(entry.SUFFIX or 0), raw))
        if not names:
            return None
        names.sort(key=lambda t: (t[0] not in (0x00, 0x20), t[0] != 0x00))
        return names[0][1]
    except Exception as e:
        log.debug("NetBIOS %s fallita: %s", ip, e)
        return None


def _mdns_query(ip, timeout, qu):
    """PTR reverse unicast a ip:5353. qu=True -> bit QU (risposta unicast)."""
    ptr = ".".join(reversed(str(ip).split("."))) + ".in-addr.arpa"
    dns = DNS(id=0, qr=0,
              qd=DNSQR(qname=ptr, qtype="PTR", qclass=1,
                       unicastresponse=1 if qu else 0))
    return _udp_query(bytes(dns), ip, _MDNS_PORT, timeout)


def get_mdns_name(ip, timeout=1.0):
    """mDNS reverse: query PTR unicast al device (bit QU, poi legacy)."""
    for qu in (True, False):
        try:
            data = _mdns_query(ip, timeout, qu)
            if not data:
                continue
            ans = DNS(data)
            # scapy 2.8: an e' una lista di DNSRR
            records = ans.an if isinstance(ans.an, list) else [ans.an]
            for rr in records:
                if not isinstance(rr, DNSRR) or rr.type != 12:  # PTR
                    continue
                rdata = rr.rdata
                if isinstance(rdata, bytes):
                    rdata = rdata.decode("utf-8", "replace")
                name = str(rdata).strip().rstrip(".")
                if name:
                    return name
        except Exception as e:
            log.debug("mDNS reverse %s (qu=%s) fallita: %s", ip, qu, e)
    return None


def get_system_name(ip, timeout=1.0):
    """Resolver di sistema (DNS reverse / LLMNR / NetBIOS di OS).
    Opzionale: su LAN senza DNS di solito fallisce o e' lento."""
    old = socket.getdefaulttimeout()
    try:
        socket.setdefaulttimeout(timeout)
        hostname, _, _ = socket.gethostbyaddr(ip)
        return str(hostname).strip().rstrip(".")
    except Exception:
        return None
    finally:
        socket.setdefaulttimeout(old)


def resolve(ip, cfg, force=False):
    """Metodi in ordine: NetBIOS -> mDNS reverse -> [sistema].
    Cache positiva per processo. Ritorna hostname o None."""
    if not ip:
        return None

    now = time.monotonic()
    if not force:
        hit = _cache.get(ip)
        if hit and now - hit[1] < _CACHE_TTL:
            return hit[0]

    disc = cfg.get("discovery", {})
    timeout = float(disc.get("hostname_timeout_sec", 1.0))

    methods = []
    if disc.get("hostname_netbios", True):
        methods.append(lambda: get_netbios_name(ip, timeout))
    if disc.get("hostname_mdns", True):
        methods.append(lambda: get_mdns_name(ip, timeout))
    if disc.get("hostname_system", False):
        methods.append(lambda: get_system_name(ip, timeout))

    hostname = None
    for method in methods:
        try:
            hostname = method()
        except Exception as e:
            log.debug("hostname %s: %s", ip, e)
            hostname = None
        if hostname:
            break

    if hostname:
        _cache[ip] = (hostname, now)
    return hostname


def resolve_devices(devices, cfg, max_workers=8):
    """Risolve gli hostname dei device con name vuoto (in-place, parallelo)."""
    if not cfg.get("discovery", {}).get("hostname", True):
        return devices

    targets = [d for d in devices if d.get("ip") and not (d.get("name") or "").strip()]
    if not targets:
        return devices

    log.info("Hostname: risoluzione per %d device", len(targets))
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(resolve, d["ip"], cfg): d for d in targets}
        for fut in as_completed(futures):
            dev = futures[fut]
            try:
                hostname = fut.result()
            except Exception as e:
                log.debug("hostname %s: %s", dev.get("ip"), e)
                hostname = None
            if hostname:
                dev["name"] = hostname
                log.info("Hostname: %s -> %s", dev["ip"], hostname)

    return devices
