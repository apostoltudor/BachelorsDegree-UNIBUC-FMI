from dnslib.server import DNSServer, BaseResolver
from dnslib import DNSRecord, RR, QTYPE, A, NS, RCODE, TXT
import socket
import datetime
import base64
import os

# Dimensiunea bucății de fișier pentru transfer (în octeți)
CHUNK_SIZE = 250 # Dimensiunea maximă a unui TXT record este 255 (plus 1 octet pentru lungime). Base64 va crește dimensiunea.
                 # 250 octeți de date binare encodeate Base64 vor fi aprox (250 / 3) * 4 = 333 caractere, ceea ce e OK pentru TXT.

# Directorul de bază pentru fișierele de transfer
# Asigură-te că acest director există și că serverul are permisiuni de citire
FILE_TRANSFER_BASE_DIR = "/app/files" # Calea din interiorul containerului

def is_blocked(domain, blocked_set):
    domain = domain.lower()
    if domain in blocked_set:
        return True
    for blocked_domain in blocked_set:
        if domain.endswith('.' + blocked_domain):
            return True
    return False

# Citire blocklist (asigură-te că blocklist.txt există în /app/)
try:
    with open("blocklist.txt") as f:
        blocked_domains = set(line.strip().lower() for line in f if line.strip())
except FileNotFoundError:
    print("Warning: blocklist.txt not found. Running without blocklist.")
    blocked_domains = set()

FORWARD_DNS = "1.1.1.1"  # DNS extern

# Zone custom
zones = {
    "t.example.com": {
        "NS": ["ns.t.example.com."],
        "A": {
            "ns.t.example.com": "127.0.0.1",
            "t.example.com": "10.10.10.10"
        }
    }
}

class BlocklistResolver(BaseResolver):
    def resolve(self, request, handler):
        qname = str(request.q.qname).lower().strip(".")
        labels = qname.split('.')
        qtype = QTYPE[request.q.qtype]

        # Log pentru toate interogările (pentru depanare)
        self.log_request(handler.client_address, qname, qtype)

        # === DNS TUNNEL FILE TRANSFER & TEST ===
        if len(labels) >= 3 and labels[-2:] == ['tunel', 'live']:
            # Interogare de test specifica pentru a verifica conectivitatea
            if qname == "testfile.txt.0.tunel.live":
                reply = request.reply()
                test_response_data = "Test_de_Raspuns_de_la_Server_DNS"
                reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT(test_response_data), ttl=60))
                print(f"[TUNNEL TEST] Responding to {qname} with: {test_response_data}")
                print(f"[DEBUG SEND] Prepared reply for {qname}: {reply.toZone()}") # Asta va afisa continutul raspunsului
                return reply
            
            # Logica existentă pentru transferul de fișiere
            try:
                part_id = int(labels[-3]) 
                filename = ".".join(labels[:-3])
            except ValueError:
                print(f"[ERROR] Invalid part_id in tunnel query: {labels[-3]}")
                reply = request.reply()
                reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT("INVALID_PART_ID"), ttl=60))
                return reply
            except IndexError: # Not enough parts in qname for filename.part_id.domain
                print(f"[ERROR] Malformed tunnel query (too few labels): {qname}")
                reply = request.reply()
                reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT("MALFORMED_QUERY"), ttl=60))
                return reply

            filepath = os.path.join(FILE_TRANSFER_BASE_DIR, filename)
            
            if os.path.exists(filepath):
                if qtype == "TXT":
                    reply = request.reply()
                    try:
                        with open(filepath, "rb") as f:
                            f.seek(part_id * CHUNK_SIZE)
                            chunk = f.read(CHUNK_SIZE)
                            
                            if not chunk: # End of file or invalid part_id
                                print(f"[TUNNEL] End of file or invalid part_id for {filename}, part {part_id}")
                                reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT("EOF"), ttl=60))
                            else:
                                encoded_chunk = base64.b64encode(chunk).decode('utf-8')
                                print(f"[TUNNEL] Sending chunk {part_id} for {filename} ({len(chunk)} bytes -> {len(encoded_chunk)} b64 chars)")
                                if len(encoded_chunk) > 255:
                                    reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT(encoded_chunk), ttl=60))
                                else:
                                    reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT(encoded_chunk), ttl=60))
                    except Exception as e:
                        print(f"[ERROR] Failed to read/send file chunk: {e}")
                        reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT(f"SERVER_ERROR:{e}"), ttl=60))
                    return reply
                else:
                    reply = request.reply()
                    reply.header.rcode = RCODE.NXDOMAIN # Or other appropriate error
                    reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT("UNSUPPORTED_QTYPE"), ttl=60))
                    return reply
            else:
                reply = request.reply()
                print(f"[TUNNEL] File not found: {filepath}")
                reply.add_answer(RR(qname + '.', QTYPE.TXT, rdata=TXT("FILE_NOT_FOUND"), ttl=60))
                return reply

        # === BLOCARE DOMENII ===
        if is_blocked(qname, blocked_domains):
            self.log_blocked(qname)
            reply = request.reply()
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("0.0.0.0"), ttl=60))
            return reply

        # === ZONE PERSONALIZATE ===
        for zone, records in zones.items():
            if qname == zone or qname.endswith('.' + zone.rstrip('.')):
                reply = request.reply()
                if qtype == "NS" and "NS" in records:
                    for ns in records["NS"]:
                        reply.add_answer(RR(zone, QTYPE.NS, rdata=NS(ns), ttl=60))
                    return reply
                elif qtype == "A" and qname in records.get("A", {}):
                    ip = records["A"][qname]
                    reply.add_answer(RR(qname, QTYPE.A, rdata=A(ip), ttl=60))
                    return reply
                else:
                    reply.header.rcode = RCODE.NXDOMAIN
                    return reply

        # === FORWARD DNS ===
        try:
            proxy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            proxy.settimeout(2)
            proxy.sendto(request.pack(), (FORWARD_DNS, 53))
            data, _ = proxy.recvfrom(4096)
            return DNSRecord.parse(data)
        except Exception as e:
            print(f"[ERROR] Failed to forward request for {qname}: {e}")
            # Răspunde cu un NXDOMAIN sau o eroare dacă forwarding-ul eșuează
            reply = request.reply()
            reply.header.rcode = RCODE.SERVFAIL
            return reply

    def log_blocked(self, domain):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("blocked_requests.log", "a") as log:
            log.write(f"[{now}] Blocked: {domain}\n")

    def log_request(self, client_address, domain, qtype):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("dns_requests.log", "a") as log:
            log.write(f"[{now}] From {client_address[0]}:{client_address[1]} - Query: {domain} ({qtype})\n")
        print(f"[{now}] From {client_address[0]}:{client_address[1]} - Query: {domain} ({qtype})")

if __name__ == "__main__":
    print("DNS Server running...")
    resolver = BlocklistResolver()
    try:
        server = DNSServer(resolver, port=53, address="0.0.0.0")
        server.start()
        # Keep the main thread alive to prevent the script from exiting
        import time
        while True:
            time.sleep(1)
    except Exception as e:
        print(f"Failed to start server: {e}")