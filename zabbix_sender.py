#!/usr/bin/env python3
"""Invio valori Zabbix trapper via protocollo Sender (zabbix-utils)."""

import logging

from zabbix_utils import ItemValue, Sender

log = logging.getLogger("ot.sender")


def send(cfg, values, dry_run=False):
    """values: lista di tuple (host_tecnico, key, value)."""
    if not values:
        log.info("Nessun valore da inviare")
        return None

    if dry_run:
        for host, key, value in values:
            log.info("[dry-run] %s %s=%s", host, key, value)
        return None

    sender = Sender(
        server=cfg["zabbix"]["sender_host"],
        port=int(cfg["zabbix"].get("sender_port", 10051)),
    )
    try:
        response = sender.send([ItemValue(h, k, v) for h, k, v in values])
    except Exception as e:
        log.error("Sender fallito: %s", e)
        return None

    log.info("Sender: processed=%s failed=%s total=%s",
             response.processed, response.failed, response.total)
    return response
