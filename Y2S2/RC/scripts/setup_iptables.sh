#!/bin/bash
iptables -I INPUT 6 -p udp -m udp --dport 53 -j ACCEPT
# iptables -I INPUT 6 -m state --state NEW -p tcp --dport 8080 -j ACCEPT # Nu este necesar pentru DNS UDP
netfilter-persistent save