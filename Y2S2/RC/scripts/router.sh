#!/bin/bash

# Curata TOATE regulile existente pentru a incepe de la zero
# Aceste comenzi TREBUIE sa fie inainte de orice alta regula iptables
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

# Adauga regulile specifice pentru FORWARDING

# Permite traficul deja stabilit sau related (ESENTIAL pentru raspunsuri DNS)
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

# Permite traficul DNS (UDP port 53) de la client (reteaua 172.7.0.0/16)
# catre serverul tau DNS (IP-ul specific 172.31.0.53).
iptables -A FORWARD -s 172.7.0.0/16 -d 172.31.0.53 -p udp --dport 53 -j ACCEPT

# Permite traficul DNS (UDP port 53) de la server (172.31.0.53) inapoi la client (172.7.0.x)
iptables -A FORWARD -s 172.31.0.53 -d 172.7.0.0/16 -p udp --sport 53 -j ACCEPT

# Permite ping-ul pentru debugging (ICMP)
iptables -A FORWARD -p icmp -j ACCEPT

# (Optional) Seteaza politicile default mai stricte
# iptables -P FORWARD DROP