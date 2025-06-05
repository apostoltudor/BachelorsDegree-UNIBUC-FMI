import sys
import socket
from urllib.parse import urlparse

if len(sys.argv) != 2:
    print("Usage: python3 get_ip.py <url_or_domain>")
    sys.exit(1)

input_url = sys.argv[1]

# Scoatem doar domeniul din URL
parsed_url = urlparse(input_url)
domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path

try:
    ip = socket.gethostbyname(domain)
    print(ip)
except socket.gaierror as e:
    print(f"Eroare la rezolvarea domeniului {domain}: {e}", file=sys.stderr)
    sys.exit(1)
