#!/usr/bin/env python3
from scapy.all import IPv6, sr1, ICMPv6EchoRequest
import argparse, time, ipaddress, sys

parser = argparse.ArgumentParser(description="A simple continuous ping6")
parser.add_argument("ipv6_address", help="An IPv6 address")
parser.add_argument("-i", "--interval", type=float, default=1.0,
                    help="Interval between pings in seconds (default 1s)")
args = parser.parse_args()

# Validate IPv6
try:
    ip_obj = ipaddress.IPv6Address(args.ipv6_address)
except ValueError:
    print(f"Invalid IPv6 address: {args.ipv6_address}")
    sys.exit(1)

seq = 0
try:
    while True:
        pkt = IPv6(dst=str(ip_obj)) / ICMPv6EchoRequest(seq=seq)
        reply = sr1(pkt, timeout=2, verbose=0)
        if reply:
            print(f"{reply.src} - Reply seq={seq}")
        else:
            print(f"Request timed out seq={seq}")
        seq += 1
        time.sleep(args.interval)

except KeyboardInterrupt:
    print("\nPing stopped by user")