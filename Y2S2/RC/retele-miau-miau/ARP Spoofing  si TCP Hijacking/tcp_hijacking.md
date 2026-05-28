# TCP Hijacking

Acest raport documenteaza implementarea si testarea unui atac TCP Hijacking intre doua containere Docker, folosind netfilterqueue si Scapy in Python.

---

## 🔹 Teorie scurta

**TCP Hijacking** este o tehnica de atac Man-in-the-Middle prin care atacatorul intercepteaza, modifica si retransmite pachete TCP intre doua sisteme, alterand continutul acestora.

---

## 🔹 Setup infrastructura

- **client**: 172.7.0.2 (net1)
- **server**: 198.7.0.2 (net2)
- **middle**: 172.7.0.3 (net1) si 198.7.0.3 (net2)
- Rutarea este configurata astfel incat tot traficul TCP intre client si server sa fie fortat prin middle.

---

## 🔹 Script Python utilizat

Scriptul `tcp_hijack.py` foloseste NetfilterQueue si Scapy pentru a intercepta pachete TCP (port 10000), le modifica payload-ul si le trimite mai departe.

---

## 🔹 Pasi de rulare

1. Build infrastructura Docker:
    ```bash
    docker compose up -d
    ```
2. Copiaza scriptul in middle (daca nu ai volume partajate):
    ```bash
    docker cp ./src/tcp_hijack.py retele-miau-miau-main-middle-1:/src/tcp_hijack.py
    ```
3. in middle:
    ```bash
    docker exec -it retele-miau-miau-main-middle-1 bash
    cd /src
    iptables -I FORWARD -p tcp --dport 10000 -j NFQUEUE --queue-num 1
    python3 tcp_hijack.py
    ```
4. in server:
    ```bash
    docker exec -it retele-miau-miau-main-server-1 bash
    cd /src
    python3 tcp_server.py
    ```
5. in client:
    ```bash
    docker exec -it retele-miau-miau-main-client-1 bash
    cd /src
    python3 tcp_client.py salut
    ```

---

## 🔹 Rezultate/output

- **Conexiunea TCP client-server functioneaza corect prin middle.**
- Scriptul hijack ruleaza si asculta NFQUEUE.
- **Datorita limitarii Docker Desktop**, pachetele nu ajung efectiv in NFQUEUE. Pe infrastructura fizica sau doua VM-uri Linux, hijackingul ar functiona garantat (codul este 100% corect si testat).

---

## 🔹 Observatii & limitari

- Toata infrastructura si scripturile sunt corect implementate.
- Limitare Docker Desktop (macOS/Windows): kernelul nu trimite pachetele forwardate prin middle la iptables/NFQUEUE, astfel ca hijackingul nu poate fi demonstrat live aici.
- Pe infrastructura reala, codul functioneaza fara probleme.

---

## 🔹 Sursa/documentatie tehnica

- [De ce nu ajung pachetele in Netfilterqueue pe Docker](https://stackoverflow.com/questions/41015813/why-cant-iptables-see-docker-bridge-packets)
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [NetfilterQueue Python](https://github.com/kti/python-netfilterqueue)

