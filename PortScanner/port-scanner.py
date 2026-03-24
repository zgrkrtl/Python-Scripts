#!/usr/bin/env python3
import socket
import ipaddress
import re

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

print(r"""
  ____  _____  ____  _   _ ____  
 / __ \|__  / / ___|| | | |  _ \ 
| |  | | / / | |  _ | | | | |_) |
| |__| |/ /_ | |_| || |_| |  _ < 
 \____/|____| \____| \___/|_| \_\
                                  
        P O R T   S C A N N E R  
""")
print("****************************************************************")
print("*                                                              *")
print("* Port Scanner by Ozgur                                       *")
print("*                                                              *")
print("****************************************************************")

open_ports = []

while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalid ip address")

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

print(f"\nScanning {ip_add_entered} from port {port_min} to {port_max}...\n")

for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_ports.append(port)
    except:
        pass

if open_ports:
    for port in open_ports:
        print(f"Port {port} is open on {ip_add_entered}.")
else:
    print("No open ports found in the given range.")