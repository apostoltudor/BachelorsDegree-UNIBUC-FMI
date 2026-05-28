# ARP Spoofing

Acest raport documenteaza implementarea si demonstrarea unui atac ARP Spoofing intre containere Docker, folosind Python (Scapy) in infrastructura multi-network (net1/net2).

---

## 🔹 Teorie scurta

**ARP spoofing** (Address Resolution Protocol spoofing) presupune trimiterea de mesaje ARP false intr-o retea locala pentru a asocia adresa IP a unui sistem cu adresa MAC a atacatorului, facilitand interceptarea traficului (Man-in-the-Middle).

---

## 🔹 Setup infrastructura

- **client**: 172.7.0.2 (net1)
- **server**: 198.7.0.2 (net2)
- **middle**: 172.7.0.3 (net1) si 198.7.0.3 (net2)
- **router**: asigura legatura intre net1 si net2
- Rutarea a fost configurata astfel incat tot traficul sa treaca prin middle.

---

## 🔹 Script Python utilizat

Scriptul `arp_spoof.py` foloseste Scapy pentru a trimite pachete ARP false periodic, mintind routerul si clientul ca middle este detinatorul adreselor IP din retea.

---

## 🔹 Pasi de rulare

1. Build infrastructura Docker:
    ```bash
    docker compose up -d
    ```
2. Intra in containerul middle si ruleaza scriptul:
    ```bash
    docker exec -it retele-miau-miau-main-middle-1 bash
    cd /src
    python3 arp_spoof.py
    ```
3. Verifica tabela ARP in router:
    ```bash
    docker exec -it retele-miau-miau-main-router-1 bash
    ip neigh
    ```
4. (Optional) Verifica tabela ARP si in client (desi pe Docker aceasta nu se otraveste).

---

## 🔹 Rezultate/output

- **in router**, dupa rularea atacului:
    ```
    198.7.0.3 dev eth0 lladdr fa:28:63:a6:8d:22 REACHABLE
    ```
- **Pe client**, tabela ARP nu a fost otravita (limita Docker, explicata mai jos).
- Traficul dintre client si server a trecut fizic prin middle (MITM logic realizat).

---

## 🔹 Observatii & limitari

- Atacul ARP Spoofing functioneaza complet pe partea de router.
- **Limita Docker Desktop:** Bridge-ul izoleaza layer 2, deci tabela ARP din client nu poate fi otravita prin middle. Pe infrastructura reala sau pe doua VM-uri conectate la aceeasi retea, ar functiona complet.
- Codul si pasii sunt compatibili cu infrastructura fizica.

---

## 🔹 Referinte

- [Scapy ARP Spoofing docs](https://scapy.readthedocs.io/)
- [Limitari Docker la ARP Spoofing](https://stackoverflow.com/questions/48635590/arp-spoofing-in-docker-containers)
