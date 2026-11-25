#!/usr/bin/env python3
"""OT Line Zabbix head.
Scopre i device della linea (ARP + PROFINET DCP + EtherNet/IP CIP), li classifica
(allen_bradley / siemens / ethernetip / profinet / pc / generic), sincronizza gli
host Zabbix via API (un host per device, template per tipo) e invia lo stato
via trapper Sender.
"""

import argparse
import logging
import logging.handlers
import os
import signal
import sys
import time
import zabbix_utils

import yaml

import discovery
import readers
from zabbix_api import ZabbixApi, technical_name
from zabbix_sender import send

log = logging.getLogger("ot.main")

stop_requested = False


def _handle_signal(signum, _frame):
    global stop_requested
    log.info("Segnale %s ricevuto, arresto dopo il ciclo corrente...", signum)
    stop_requested = True


def load_config(path):
    with open(path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)

    env_token = os.environ.get("ZABBIX_API_TOKEN")
    if env_token:
        cfg["zabbix"]["api_token"] = env_token

    token = cfg["zabbix"].get("api_token") or ""
    if not token or token == "REPLACE_ME":
        raise RuntimeError("API token mancante: configura zabbix.api_token o la env ZABBIX_API_TOKEN")

    return cfg


def setup_logging(cfg):
    log_cfg = cfg.get("logging", {})
    level = getattr(logging, str(log_cfg.get("level", "INFO")).upper(), logging.INFO)
    fmt = logging.Formatter("%(asctime)s %(levelname)-7s %(name)s: %(message)s")

    root = logging.getLogger()
    root.setLevel(level)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(fmt)
    root.addHandler(console)

    log_file = log_cfg.get("file")
    if log_file:
        handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
        )
        handler.setFormatter(fmt)
        root.addHandler(handler)


def run_discovery_cycle(api, cfg, ifaces, known, last_seen, unseen_counts):
    """Discovery completa + sync API + invio stato/letture. Ritorna True se ok."""
    log.info("--- Ciclo discovery ---")

    try:
        devices = discovery.discover_all(ifaces, cfg)
        readers.enrich(devices, cfg)
        sendable = api.sync(devices, cfg, unseen_counts)
    except Exception:
        log.exception("Ciclo discovery fallito")
        return False

    now = int(time.time())
    values = []

    for dev in devices:
        ip = dev.get("ip")
        if not ip:
            continue
        host = technical_name(cfg, ip)
        known[host] = ip

        if host not in sendable:
            log.debug("Host %s non inviabile (disabilitato/ignoto), salto", host)
            continue

        last_seen[host] = now
        values.append((host, "dev.reachable", 1))
        values.append((host, "dev.last_seen", now))

        if dev.get("keyswitch"):
            values.append((host, "ab.keyswitch", str(dev["keyswitch"])))

    # prune host disabilitati da known
    for host in list(known):
        if unseen_counts.get(host, 0) >= int(cfg["intervals"].get("disable_after", 3)):
            if host not in sendable:
                known.pop(host, None)
                last_seen.pop(host, None)

    send(cfg, values, dry_run=api.dry_run)
    log.info("Discovery: %d device, %d valori inviati", len(devices), len(values))
    return True


def run_status_cycle(cfg, ifaces, known, last_seen, dry_run=False):
    """Ciclo veloce: ARP (su ogni interfaccia) + ping fallback -> dev.reachable / dev.last_seen."""
    if not known:
        return

    log.debug("--- Ciclo stato (%d host noti) ---", len(known))
    live_ips = set()
    for iface in ifaces:
        live_ips.update(
            d["ip"] for d in discovery.arp_scan(
                iface["ip"], iface["netmask"], iface["name"], timeout_sec=1
            )
        )

    now = int(time.time())
    values = []

    for host, ip in known.items():
        reachable = ip in live_ips or discovery.ping(ip)
        values.append((host, "dev.reachable", 1 if reachable else 0))
        if reachable:
            last_seen[host] = now
            values.append((host, "dev.last_seen", now))

    send(cfg, values, dry_run=dry_run)


def main():
    parser = argparse.ArgumentParser(description="OT Line Zabbix head")
    parser.add_argument("--config", default="config.yaml", help="Percorso config YAML")
    parser.add_argument("--iface", default=None,
                        help="Override line.iface (nome/IP separati da virgola, o 'auto')")
    parser.add_argument("--dry-run", action="store_true",
                        help="Scopre e classifica ma non tocca Zabbix (nessuna API/scrittura)")
    parser.add_argument("--once", action="store_true",
                        help="Un solo ciclo discovery e poi esce")
    args = parser.parse_args()

    cfg = load_config(args.config)
    setup_logging(cfg)

    if args.iface:
        cfg["line"]["iface"] = args.iface

    ifaces = discovery.resolve_interfaces(cfg["line"]["iface"])
    for iface in ifaces:
        log.info("Interfaccia: %s (%s/%s)", iface["name"], iface["ip"], iface["netmask"])

    api = ZabbixApi(cfg["zabbix"]["api_url"], cfg["zabbix"]["api_token"], dry_run=args.dry_run)

    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    status_interval = int(cfg["intervals"].get("status_sec", 60))
    discovery_interval = int(cfg["intervals"].get("discovery_sec", 900))

    known = {}        # host tecnico -> ip
    last_seen = {}    # host tecnico -> unix ts
    unseen_counts = {}  # host tecnico -> cicli discovery senza risposta

    next_discovery = 0.0
    next_status = 0.0

    while not stop_requested:
        now = time.monotonic()

        if now >= next_discovery:
            if not args.once:
                run_discovery_cycle(api, cfg, ifaces, known, last_seen, unseen_counts)
            else:
                try:
                    devices = discovery.discover_all(ifaces, cfg)
                    readers.enrich(devices, cfg)
                    api.sync(devices, cfg, unseen_counts)
                    for dev in devices:
                        log.info("%-15s %-14s %-22s %s",
                                 dev.get("ip", ""), dev.get("type", ""),
                                 (dev.get("name") or "")[:22], dev.get("vendor", ""))
                except Exception:
                    log.exception("Discovery fallita")
                    sys.exit(1)
                return
            next_discovery = time.monotonic() + discovery_interval
            next_status = time.monotonic() + status_interval
        elif now >= next_status:
            try:
                run_status_cycle(cfg, ifaces, known, last_seen, dry_run=args.dry_run)
            except Exception:
                log.exception("Ciclo stato fallito")
            next_status = time.monotonic() + status_interval

        time.sleep(1)

    log.info("Arrestato.")


if __name__ == "__main__":
    main()
