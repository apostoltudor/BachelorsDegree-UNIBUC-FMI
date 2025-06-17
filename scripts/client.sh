#!/bin/bash
set -x

ip link set eth0 up
ip route del default || true

ip route add default via 172.7.0.3 dev eth0

echo "nameserver 8.8.8.8" >> /etc/resolv.conf
