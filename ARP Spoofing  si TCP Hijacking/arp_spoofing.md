# ARP Spoofing

Acest raport documentează implementarea și demonstrarea unui atac ARP Spoofing între containere Docker, folosind Python (Scapy) în infrastructură multi-network (net1/net2).

---

## 🔹 Teorie scurtă

**ARP spoofing** (Address Resolution Protocol spoofing) presupune trimiterea de mesaje ARP false într-o rețea locală pentru a asocia adresa IP a unui sistem cu adresa MAC a atacatorului, facilitând interceptarea traficului (Man-in-the-Middle).

---

## 🔹 Setup infrastructură

- **client**: 172.7.0.2 (net1)
- **server**: 198.7.0.2 (net2)
- **middle**: 172.7.0.3 (net1) și 198.7.0.3 (net2)
- **router**: asigură legătura între net1 și net2
- Rutarea a fost configurată astfel încât tot traficul să treacă prin middle.

---

## 🔹 Script Python utilizat

Scriptul `arp_spoof.py` folosește Scapy pentru a trimite pachete ARP false periodic, mințind routerul și clientul că middle este deținătorul adreselor IP din rețea.

---

## 🔹 Pași de rulare

1. Build infrastructură Docker:
    ```bash
    docker compose up -d
    ```
2. Intră în containerul middle și rulează scriptul:
    ```bash
    docker exec -it retele-miau-miau-main-middle-1 bash
    cd /src
    python3 arp_spoof.py
    ```
3. Verifică tabela ARP în router:
    ```bash
    docker exec -it retele-miau-miau-main-router-1 bash
    ip neigh
    ```
4. (Opțional) Verifică tabela ARP și în client (deși pe Docker aceasta nu se otrăvește).

---

## 🔹 Rezultate/output

- **În router**, după rularea atacului:
    ```
    198.7.0.3 dev eth0 lladdr fa:28:63:a6:8d:22 REACHABLE
    ```
- **Pe client**, tabela ARP nu a fost otrăvită (limita Docker, explicată mai jos).
- Traficul dintre client și server a trecut fizic prin middle (MITM logic realizat).

---

## 🔹 Observații & limitări

- Atacul ARP Spoofing funcționează complet pe partea de router.
- **Limita Docker Desktop:** Bridge-ul izolează layer 2, deci tabela ARP din client nu poate fi otrăvită prin middle. Pe infrastructură reală sau pe două VM-uri conectate la aceeași rețea, ar funcționa complet.
- Codul și pașii sunt compatibili cu infrastructură fizică.

---

## 🔹 Referințe

- [Scapy ARP Spoofing docs](https://scapy.readthedocs.io/)
- [Limitări Docker la ARP Spoofing](https://stackoverflow.com/questions/48635590/arp-spoofing-in-docker-containers)
