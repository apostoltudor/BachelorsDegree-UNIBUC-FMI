root@DELL-5520:/mnt/c/Users/Dell/retele-miau-miau# dig @127.0.0.1 -p 55555 www.accuweather.com

root@DELL-5520:/mnt/c/Users/Dell/retele-miau-miau# docker exec -it dns_blocker bash
root@493bcfc79380:/app# python3 generate_stats.py
root@493bcfc79380:/app# python3 blocked_stats_companies.py