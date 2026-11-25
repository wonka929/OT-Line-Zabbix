#!/usr/bin/env python3
"""
Siemens S7 PLC Information Enumeration
Translated from nmap's s7-info.nse script
"""

import socket
import struct
import sys
import argparse
from typing import Optional, Dict


class S7Info:
    COTP = bytes.fromhex("0300001611e00000001400c1020100c2020102c0010a")
    ALT_COTP = bytes.fromhex("0300001611e00000000500c1020100c2020200c0010a")
    ROSCTR_SETUP = bytes.fromhex("0300001902f08032010000000000080000f0000001000101e0")
    READ_SZL = bytes.fromhex("0300002102f080320700000000000800080001120411440100ff09000400110001")
    FIRST_SZL_REQUEST = bytes.fromhex("0300002102f080320700000000000800080001120411440100ff09000400110001")
    SECOND_SZL_REQUEST = bytes.fromhex("0300002102f080320700000000000800080001120411440100ff090004001c0001")

    def __init__(self, host: str, port: int = 102, timeout: float = 10.0, verbose: bool = False):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.verbose = verbose
        self.sock: Optional[socket.socket] = None

    def log(self, msg: str):
        if self.verbose:
            print(f"[*] {msg}", file=sys.stderr)

    def connect(self) -> bool:
        self.close()
        try:
            self.log(f"Connecting to {self.host}:{self.port}")
            self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
            self.sock.settimeout(self.timeout)
            return True
        except (socket.timeout, ConnectionRefusedError, OSError) as e:
            self.log(f"Connection error: {e}")
            return False

    def close(self):
        if self.sock:
            try:
                self.sock.close()
            except OSError:
                pass
            self.sock = None

    def send_receive(self, data: bytes, min_bytes: int) -> Optional[bytes]:
        if not self.sock:
            return None
        try:
            self.sock.sendall(data)
            response = b""
            while len(response) < min_bytes:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                response += chunk
            self.log(f"Sent {len(data)} bytes, received {len(response)} bytes")
            return response if len(response) >= min_bytes else None
        except socket.timeout:
            self.log(f"Timeout waiting for response (got {len(response)} of {min_bytes} bytes)")
            return None
        except OSError as e:
            self.log(f"Send/receive error: {e}")
            return None

    def try_cotp(self) -> bool:
        self.log("Trying COTP (rack 01, slot 02)...")
        response = self.send_receive(self.COTP, 6)
        if response and len(response) >= 6 and response[5] == 0xd0:
            self.log("COTP connected successfully")
            return True
        self.log(f"COTP failed, PDU type: {hex(response[5]) if response and len(response) >= 6 else 'no response'}")
        return False

    def try_alt_cotp(self) -> bool:
        self.log("Trying alt COTP (rack 02, slot 00)...")
        response = self.send_receive(self.ALT_COTP, 6)
        if response and len(response) >= 6 and response[5] == 0xd0:
            self.log("Alt COTP connected successfully")
            return True
        self.log(f"Alt COTP failed, PDU type: {hex(response[5]) if response and len(response) >= 6 else 'no response'}")
        return False

    def parse_first_response(self, response: bytes) -> Dict[str, str]:
        output = {}
        if len(response) < 125 or response[7] != 0x32:
            self.log(f"First SZL response invalid: len={len(response)}, proto={hex(response[7]) if len(response) > 7 else '?'}")
            return output

        module_end = response.find(b'\x00', 43)
        if module_end > 43:
            output["Module"] = response[43:module_end].decode('ascii', errors='ignore')

        hw_end = response.find(b'\x00', 71)
        if hw_end > 71:
            output["Basic Hardware"] = response[71:hw_end].decode('ascii', errors='ignore')

        if len(response) >= 125:
            char1, char2, char3 = response[122], response[123], response[124]
            output["Version"] = f"{char1}.{char2}.{char3}"

        return output

    def parse_second_response(self, response: bytes) -> Dict[str, str]:
        output = {}
        if len(response) < 32 or response[7] != 0x32:
            self.log(f"Second SZL response invalid: len={len(response)}")
            return output

        szl_id = response[30]
        offset = 4 if szl_id != 0x1c else 0
        self.log(f"Second SZL: szl_id=0x{szl_id:02x}, offset={offset}")

        def extract_string(start: int) -> Optional[str]:
            if len(response) <= start:
                return None
            end = response.find(b'\x00', start)
            if end > start:
                return response[start:end].decode('ascii', errors='ignore')
            return None

        fields = {
            "System Name": 39 + offset,
            "Module Type": 73 + offset,
            "Plant Identification": 107 + offset,
            "Copyright": 141 + offset,
            "Serial Number": 175 + offset,
        }

        for key, start in fields.items():
            val = extract_string(start)
            if val:
                output[key] = val

        return output

    def run(self) -> Optional[Dict[str, str]]:
        if not self.connect():
            return None

        try:
            # Step 1: COTP handshake - try primary, then alt with fresh socket
            if not self.try_cotp():
                # Must create a NEW socket for alt COTP (matches nmap behavior)
                if not self.connect():
                    return None
                if not self.try_alt_cotp():
                    self.log("Could not negotiate COTP")
                    return None

            # Step 2: ROSCTR setup
            self.log("Sending ROSCTR setup...")
            response = self.send_receive(self.ROSCTR_SETUP, 8)
            if not response or len(response) < 8 or response[7] != 0x32:
                self.log("ROSCTR setup failed")
                return None

            # Step 3: Read SZL
            self.log("Sending Read SZL...")
            response = self.send_receive(self.READ_SZL, 8)
            if not response or len(response) < 8 or response[7] != 0x32:
                self.log("Read SZL failed")
                return None

            # Step 4: First SZL request (basic hardware + version)
            self.log("Sending first SZL request...")
            response = self.send_receive(self.FIRST_SZL_REQUEST, 125)
            if not response:
                self.log("No response to first SZL request")
                return None
            output = self.parse_first_response(response)
            self.log(f"First SZL parsed: {output}")

            # Step 5: Second SZL request (system name, serial, etc.)
            self.log("Sending second SZL request...")
            response = self.send_receive(self.SECOND_SZL_REQUEST, 180)
            if response:
                second = self.parse_second_response(response)
                self.log(f"Second SZL parsed: {second}")
                output.update(second)

            return output if output else None

        finally:
            self.close()


#def main():
#    parser = argparse.ArgumentParser(description="Enumerate Siemens S7 PLC device information")
#    parser.add_argument("host", help="Target host IP address")
#    parser.add_argument("-p", "--port", type=int, default=102, help="Target port (default: 102)")
#    parser.add_argument("-t", "--timeout", type=float, default=10.0, help="Socket timeout in seconds (default: 10.0)")
#    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose/debug output")
#
#    args = parser.parse_args()
#
#    s7 = S7Info(args.host, args.port, args.timeout, args.verbose)
#    result = s7.run()
#
#    if result:
#        print(f"S7 PLC Information for {args.host}:{args.port}")
#        print("-" * 40)
#        for key, value in result.items():
#            print(f"  {key}: {value}")
#        sys.exit(0)
#    else:
#        print(f"No S7 PLC found at {args.host}:{args.port}")
#        sys.exit(1)
#
#
#if __name__ == "__main__":
#    main()
