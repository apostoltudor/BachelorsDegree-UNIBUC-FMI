from dnslib import DNSRecord, QTYPE
import base64
import socket

def request_chunk(filename, part_id, dns_server="172.31.0.53"):
    domain = f"{filename}.{part_id}.tunel.live"
    q = DNSRecord.question(domain, qtype="TXT")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(q.pack(), (dns_server, 53))
    data, _ = s.recvfrom(1024)
    reply = DNSRecord.parse(data)
    for rr in reply.rr:
        if rr.rtype == QTYPE.TXT:
            return rr.rdata.data[0].decode()
    return None

def download_file(filename):
    part_id = 0
    with open(f"received_{filename}", "wb") as f:
        while True:
            txt = request_chunk(filename, part_id)
            if txt == "EOF":
                break
            chunk = base64.b64decode(txt)
            f.write(chunk)
            part_id += 1
            print(f"Received part {part_id}")

if __name__ == "__main__":
    download_file("testfile.txt")
