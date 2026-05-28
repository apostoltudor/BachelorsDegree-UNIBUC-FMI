import sys
import socket
from urllib.parse import urlparse

# Verificam ca scriptul sa fie apelat cu exact un argument (URL sau domeniu)
if len(sys.argv) != 2:
    print("Usage: python3 get_ip.py <url_or_domain>")
    sys.exit(1)

input_url = sys.argv[1]

# Parsam URL-ul pentru a extrage domeniul
parsed_url = urlparse(input_url)

# Daca avem un URL complet (ex: https://site.com), luam netloc (site.com)
# Altfel, luam direct argumentul ca domeniu (ex: site.com fara schema)
domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path

try:
    # Rezolvam IP-ul asociat domeniului
    ip = socket.gethostbyname(domain)
    print(ip)
except socket.gaierror as e:
    # Daca rezolvarea DNS esueaza, afisam eroarea la stderr
    print(f"Eroare la rezolvarea domeniului {domain}: {e}", file=sys.stderr)
    sys.exit(1)
