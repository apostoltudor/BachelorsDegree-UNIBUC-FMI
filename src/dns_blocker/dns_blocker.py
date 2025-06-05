from dnslib.server import DNSServer, BaseResolver
from dnslib import DNSRecord, RR, QTYPE, A
import socket
import datetime

# Citește blocklist-ul
with open("blocklist.txt") as f:
    blocked_domains = set(line.strip().lower() for line in f if line.strip())

FORWARD_DNS = "1.1.1.1"  # DNS extern, poate fi și 8.8.8.8

class BlocklistResolver(BaseResolver):
    def resolve(self, request, handler):
        qname = str(request.q.qname).rstrip(".").lower()
        qtype = QTYPE[request.q.qtype]

        if qname in blocked_domains:
            self.log_blocked(qname)
            reply = request.reply()
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("0.0.0.0"), ttl=60))
            return reply

        # Forward către DNS real
        try:
            proxy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            proxy.settimeout(2)
            proxy.sendto(request.pack(), (FORWARD_DNS, 53))
            data, _ = proxy.recvfrom(4096)
            return DNSRecord.parse(data)
        except Exception as e:
            print(f"[ERROR] Failed to forward request for {qname}: {e}")
            return request.reply()  # răspuns gol dacă nu reușește forward

    def log_blocked(self, domain):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("blocked_requests.log", "a") as log:
            log.write(f"[{now}] Blocked: {domain}\n")


if __name__ == "__main__":
    print("DNS Server running on port 53...")
    resolver = BlocklistResolver()
    server = DNSServer(resolver, port=53, address="0.0.0.0")
    server.start()
