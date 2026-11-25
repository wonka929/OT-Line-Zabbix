#!/usr/bin/env python3
"""Lettura identificativa WAGO via Modbus TCP (FC 0x03).

I WAGO spesso non espongono CIP (44818) ne' PROFINET/S7 (102): l'unico accesso
ai dati identificativi e' Modbus TCP (porta 502). Registri holding:
  0x2010  firmware revision
  0x2011  series
  0x2012  item
  0x2013  firmware major
  0x2014  firmware minor
  0x2020  descrizione breve (16 word ASCII)
"""

import logging
import socket
import struct

log = logging.getLogger("ot.wago")

REG_FW_REV = 0x2010
REG_SERIES = 0x2011
REG_ITEM = 0x2012
REG_FW_MAJOR = 0x2013
REG_FW_MINOR = 0x2014
REG_DESC = 0x2020
DESC_WORDS = 16


def read_holding_registers(sock, address, count=1, unit_id=1, transaction_id=1):
    """Invia una richiesta Modbus TCP (FC 0x03) e restituisce una tupla di registri."""
    request = struct.pack(
        ">HHHBBHH", transaction_id, 0, 6, unit_id, 0x03, address, count
    )
    sock.sendall(request)

    # 1. Legge l'intestazione MBAP (7 byte)
    mbap = b""
    while len(mbap) < 7:
        chunk = sock.recv(7 - len(mbap))
        if not chunk:
            raise ConnectionError("Connessione chiusa dal dispositivo")
        mbap += chunk

    _, _, length, _ = struct.unpack(">HHHB", mbap)

    # 2. Legge il PDU (length - 1 byte)
    pdu_len = length - 1
    pdu = b""
    while len(pdu) < pdu_len:
        chunk = sock.recv(pdu_len - len(pdu))
        if not chunk:
            raise ConnectionError("Connessione chiusa durante la lettura dei dati")
        pdu += chunk

    # Estrae Function Code (1° byte) e Byte Count / Exception Code (2° byte)
    func_code, second_byte = struct.unpack(">BB", pdu[:2])

    # Gestione eccezione Modbus
    if func_code & 0x80:
        raise RuntimeError(
            f"Eccezione Modbus 0x{second_byte:02X} all'indirizzo 0x{address:04X}"
        )

    data = pdu[2 : 2 + second_byte]
    return struct.unpack(f">{count}H", data)


def read_wago_info(ip, timeout=3.0, port=502, unit_id=1):
    """Legge i registri identificativi WAGO via Modbus TCP.

    Restituisce dict {product_type, firmware, description} (campi vuoti se
    assenti); dict vuoto se il device non e' raggiungibile o non risponde.
    """
    try:
        with socket.create_connection((ip, port), timeout=timeout) as s:
            s.settimeout(timeout)
            tid = 0

            def reg(address, count=1):
                nonlocal tid
                tid += 1
                return read_holding_registers(
                    s, address, count=count, unit_id=unit_id, transaction_id=tid
                )

            (fw_rev,) = reg(REG_FW_REV)
            (series,) = reg(REG_SERIES)
            (item,) = reg(REG_ITEM)
            (fw_major,) = reg(REG_FW_MAJOR)
            (fw_minor,) = reg(REG_FW_MINOR)
            desc_regs = reg(REG_DESC, count=DESC_WORDS)
    except Exception as e:
        log.debug("Modbus WAGO %s fallita: %s", ip, e)
        return {}

    raw_bytes = struct.pack(f">{len(desc_regs)}H", *desc_regs)
    description = raw_bytes.decode("ascii", errors="ignore").rstrip("\x00").strip()

    return {
        "product_type": f"{series}-{item}",
        "firmware": f"{fw_major:02d}.{fw_minor:02d} (Rev. {fw_rev})",
        "description": description,
    }


if __name__ == "__main__":
    # Test manuale via tunnel SSH: python wago.py <ip> [port]
    import sys

    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    tcp_port = int(sys.argv[2]) if len(sys.argv) > 2 else 502
    info = read_wago_info(host, port=tcp_port)
    if not info:
        print(f"Nessuna risposta Modbus da {host}:{tcp_port}")
    else:
        print(f"Dispositivo: {info['product_type']}")
        print(f"Firmware:    {info['firmware']}")
        print(f"Descrizione: {info['description']}")
