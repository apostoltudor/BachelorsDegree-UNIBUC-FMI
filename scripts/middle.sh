#!/bin/bash
set -x

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Add 8.8.8.8 nameserver (optional, but good for middle if it needs to resolve)
echo "nameserver 8.8.8.8" >> /etc/resolv.conf

# We need to drop the kernel reset of hand-coded tcp connections
iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP


# === CRITICAL ROUTE FORWARDING FOR MIDDLE ===
# The default gateway for middle should be the router's IP on net2.
# First, remove any existing default route that might be incorrect.
ip route del default || true # Delete if it exists, ignore error if it doesn't

# Add the default route via the router's IP on net2 (198.7.0.1)
# This means all traffic not explicitly for 172.7.0.0/16 or 198.7.0.0/16
# will be sent to 198.7.0.1 (the router)
ip route add default via 198.7.0.1 dev eth1 # eth1 is the interface connected to net2

# Allow traffic from net1 (client) to net2 (router)
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
# Allow traffic from net2 (router) to net1 (client) for responses
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
# Allow established/related connections
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT