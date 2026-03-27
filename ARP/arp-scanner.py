from scapy.all import ARP, Ether, srp

target = "10.0.2.0/24"
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target)

ans, unans = srp(packet, timeout=3, verbose=0)

print(f"{'IP Address':<20} {'MAC Address'}")
print("-" * 40)

for sent_pkt, received_pkt in ans:
    print(f"{received_pkt[ARP].psrc:<20} {received_pkt[ARP].hwsrc}")

print(f"\n{len(ans)} hosts found, {len(unans)} no response")