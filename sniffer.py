from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] Source: {ip_src} -> Destination: {ip_dst} | Protocol: {proto}")
        if TCP in packet:
            print("TCP Payload:", bytes(packet[TCP].payload))
        elif UDP in packet:
            print("UDP Payload:", bytes(packet[UDP].payload))
        print("=" * 60)

print("🔎 Sniffing Started... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
