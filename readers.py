#!/usr/bin/env python3
"""Letture base device: Siemens SZL via porta 102 (s7_info), Allen-Bradley
LogixDriver.info e WAGO identificativi via Modbus TCP (porta 502)."""

import logging

import s7_info
import wago

log = logging.getLogger("ot.readers")


def read_siemens(ip, timeout_sec=5):
    """SZL S7: module, version, serial, system name. Restituisce dict (vuoto se fallisce)."""
    try:
        data = s7_info.S7Info(ip, timeout=timeout_sec).run()
    except Exception as e:
        log.debug("S7 SZL %s fallita: %s", ip, e)
        return {}
    if not data:
        return {}

    return {
        "firmware": data.get("Version", ""),
        "serial": data.get("Serial Number", ""),
        "product_type": data.get("Module") or data.get("Module Type", ""),
        "system_name": data.get("System Name", ""),
    }


def read_allen_bradley(ip):
    """LogixDriver.info: keyswitch/mode, nome PLC, revision, serial.
    Solo PLC Logix (ControlLogix/CompactLogix/Micro800): altri device CIP restituiscono dict vuoto."""
    try:
        from pycomm3 import LogixDriver

        with LogixDriver(ip, init_tags=False, init_info=True) as plc:
            info = dict(plc.info or {})
    except Exception as e:
        log.debug("LogixDriver.info %s fallita (non-Logix o offline): %s", ip, e)
        return {}

    rev = info.get("revision", "")
    return {
        "keyswitch": str(info.get("keyswitch", "") or ""),
        "system_name": str(info.get("name", "") or ""),
        "firmware": str(rev),
        "serial": str(info.get("serial", "") or ""),
        "product_type": str(info.get("device_type") or info.get("product_type") or ""),
    }


def read_wago(ip, timeout_sec=3.0, port=502):
    """Modbus TCP (FC 0x03): registri identificativi WAGO 0x2010-0x2020.
    Per i WAGO che non rispondono ne' a CIP (44818) ne' a PROFINET (102)."""
    return wago.read_wago_info(ip, timeout=timeout_sec, port=port)


def enrich(devices, cfg):
    """Arricchisce i device classificati con le letture base (merge solo campi vuoti). In-place."""
    reads = cfg.get("reads", {})

    for dev in devices:
        ip = dev.get("ip")
        if not ip:
            continue

        if dev.get("type") == "siemens" and reads.get("s7_szl", True):
            extra = read_siemens(ip)
            for key, value in extra.items():
                if value and not dev.get(key):
                    dev[key] = value

        if dev.get("type") == "allen_bradley" and reads.get("ab_keyswitch", True):
            extra = read_allen_bradley(ip)
            for key, value in extra.items():
                if value and not dev.get(key):
                    dev[key] = value

        # WAGO visti solo da ARP/DCP (nessuna risposta CIP/PROFINET): Modbus TCP
        vendor = (dev.get("vendor") or "").lower()
        seen = set(dev.get("seen_by") or [])
        if (
            reads.get("wago_modbus", True)
            and "wago" in vendor
            and not seen & {"CIP", "PROFINET"}
        ):
            extra = read_wago(
                ip,
                timeout_sec=reads.get("wago_modbus_timeout", 3.0),
                port=reads.get("wago_modbus_port", 502),
            )
            for key, value in extra.items():
                if value and not dev.get(key):
                    dev[key] = value

    return devices
