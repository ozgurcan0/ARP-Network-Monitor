import sys
import time
from scapy.all import ARP, Ether, srp

def get_ip_block():
    if len(sys.argv) != 2:
        print("Usage: python main.py <IP_BLOCK>")
        sys.exit(1)
    return sys.argv[1]

def get_arp_table(ip_block):
    arp = ARP(pdst=ip_block)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=False)[0]
    arp_table = {}
    
    for sent, received in result:
        arp_table[received.psrc] = received.hwsrc

    return arp_table

def monitor_network(ip_block):
    previous_arp_table = {}
    
    while True:
        print(f"\n{time.ctime()}: Checking network...")
        current_arp_table = get_arp_table(ip_block)

        for ip, mac in current_arp_table.items():
            if ip in previous_arp_table:
                if previous_arp_table[ip] != mac:
                    print(f"[!] MAC address changed! IP: {ip}, Old MAC: {previous_arp_table[ip]}, New MAC: {mac}")
            else:
                print(f"[+] New device detected! IP: {ip}, MAC: {mac}")

        previous_arp_table = current_arp_table
        time.sleep(10)

def main():
    ip_block = get_ip_block()
    monitor_network(ip_block)

if __name__ == "__main__":
    main()
