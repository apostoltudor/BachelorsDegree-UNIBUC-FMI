#!/bin/bash

# Alege un website (doar unul trebuie decomentat)
website="https://www.gov.za"
#website="https://www.une.edu.au"
#website="https://www.fudan.edu.cn/en/"

TARGET_IP=$(python3 get_ip.py $website)
TARGET_PORT=33434 # portul standard pentru traceroute

if [ -z "$TARGET_IP" ]; then
  echo "Nu s-a putut rezolva IP-ul pentru $website"
  exit 1
fi

echo "IP-ul tintei este: $TARGET_IP"
echo "Pornesc traceroute catre $TARGET_IP:$TARGET_PORT..."
python3 traceroute.py "$TARGET_IP" "$TARGET_PORT"

# verifica daca fisierul de iesire a fost creat
if [ -f "route_output.json" ]; then
  echo "Datele au fost salvate. Generez harta..."
  python3 map_trace.py route_output.json
else
  echo "Eroare: fisierul route_output.json nu a fost gasit!"
  exit 2
fi
