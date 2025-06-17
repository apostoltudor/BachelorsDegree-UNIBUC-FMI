import socket
import struct
import base64
from dnslib import DNSRecord, QTYPE

DNS_SERVER_IP = '172.31.0.53'
DNS_PORT = 53

def create_dns_query_dnslib(domain_name, query_type_str):
    q = DNSRecord.question(domain_name, query_type_str)
    return q.pack()

def parse_dns_response_dnslib(response_data):
    d = DNSRecord.parse(response_data)
    
    txt_answers = []
    for r in d.rr: 
        if r.rtype == QTYPE.TXT: # Daca este un record TXT
            # r.rdata.data este o listă de bytes (fiecare string din TXT record)
            for txt_string_bytes in r.rdata.data:
                try:
                    txt_answers.append(txt_string_bytes.decode('utf-8'))
                except UnicodeDecodeError:
                    print(f"Warning: Could not decode TXT data as UTF-8: {txt_string_bytes}")
                    txt_answers.append(str(txt_string_bytes)) # Fallback to raw bytes string
    return txt_answers

# Creare socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5) # Set timeout for response

# Interogarea pe care o vom trimite (hardcodata pentru testul actual)
domain_to_query = "testfile.txt.0.tunel.live"
query_type_str = "TXT" 

query_packet = create_dns_query_dnslib(domain_to_query, query_type_str)

try:
    # Trimite interogarea
    sock.sendto(query_packet, (DNS_SERVER_IP, DNS_PORT))
    print(f"Sent DNS query for {domain_to_query} ({query_type_str}) to {DNS_SERVER_IP}:{DNS_PORT}")

    # Așteaptă răspunsul
    response_data, server_address = sock.recvfrom(4096) # Marim buffer-ul pentru raspunsuri mai mari
    print(f"Received response from {server_address[0]}:{server_address[1]}")

    # Parsează și afișează răspunsul
    answers = parse_dns_response_dnslib(response_data)
    if answers:
        print("Decoded TXT records:")
        for answer in answers:
            print(f"- {answer}")
    else:
        print("No TXT records found in response or response malformed.")

except socket.timeout:
    print("DNS query timed out. No response received from server.")
except Exception as e:
    print(f"An error occurred during DNS query: {e}")
finally:
    sock.close()