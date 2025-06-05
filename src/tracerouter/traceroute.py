import socket
import traceback
import time
import requests
import json
import sys

# # socket de UDP
# udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
# # socket RAW de citire a răspunsurilor ICMP
# icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# # setam timout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
# icmp_recv_socket.settimeout(3)

route_data = []
def is_private_ip(ip):
    return ip.startswith("10.") or ip.startswith("192.168.") or (ip.startswith("172.") and 16 <= int(ip.split('.')[1]) <= 31)

def get_geo_info(ip):
    if is_private_ip(ip):
        return {"location": "Private IP - no geo info", "lat": None, "lon": None}
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code != 200:
            return {"location": "No geo info", "lat": None, "lon": None}
        data = response.json()
        if data.get('status') == 'success':
            return {
                "location": f"{data['country']}, {data.get('regionName', '')}, {data.get('city', '')}",
                "lat": data.get("lat"),
                "lon": data.get("lon")
            }
        else:
            return {"location": "No geo info", "lat": None, "lon": None}
    except Exception as e:
        return {"location": f"Error: {e}", "lat": None, "lon": None}



def traceroute(ip, port):
    max_hops = 40
    timeout = 3
    message = b'salut'
    dest_addr = socket.gethostbyname(ip)

    print(f"Traceroute catre {dest_addr}, maxim {max_hops} hop-uri:\n")

    for ttl in range(1, max_hops + 1):
        # sockets pentru fiecare ttl
        udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
        udp_send_sock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        icmp_recv_socket.settimeout(timeout)

        # bind pe portul local
        icmp_recv_socket.bind(("", port))

        start_time = time.time()

        try:
            udp_send_sock.sendto(message, (dest_addr, port))
            data, addr = icmp_recv_socket.recvfrom(512)

            end_time = time.time()

            elapsed = (end_time - start_time) * 1000  # ms
            router_ip = addr[0]

            # verificam daca e un mesaj ICMP Port Unreachable => destinatie atinsa
            icmp_type = data[20]
            geo = get_geo_info(router_ip)
            if icmp_type == 3:
                print(f"{ttl}\t{router_ip}\t{round(elapsed, 2)} ms\t{geo['location']} (DESTINATION REACHED)")
                route_data.append({
                    "ttl": ttl,
                    "ip": router_ip,
                    "elapsed_ms": round(elapsed, 2),
                    "location": geo["location"],
                    "lat": geo["lat"],
                    "lon": geo["lon"]
                })
                break
            elif icmp_type == 11:
                print(f"{ttl}\t{router_ip}\t{round(elapsed, 2)} ms\t{geo['location']}")
            else:
                print(f"{ttl}\t{router_ip}\t{round(elapsed, 2)} ms\t{geo['location']} (ICMP type {icmp_type})")

            route_data.append({
                "ttl": ttl,
                "ip": router_ip,
                "elapsed_ms": round(elapsed, 2),
                "location": geo["location"],
                "lat": geo["lat"],
                "lon": geo["lon"]
            })

        except socket.timeout:
            print(f"{ttl}\t* * * Request timed out")
        except Exception as e:
            print(f"{ttl}\tError: {e}")
            print(traceback.format_exc())

        finally:
            udp_send_sock.close()
            icmp_recv_socket.close()

'''
 Exercitiu hackney carriage (optional)!
    e posibil ca ipinfo sa raspunda cu status code 429 Too Many Requests
    cititi despre campul X-Forwarded-For din antetul HTTP
        https://www.nginx.com/resources/wiki/start/topics/examples/forwarded/
    si setati-l o valoare in asa fel incat
    sa puteti trece peste sistemul care limiteaza numarul de cereri/zi

    Alternativ, puteti folosi ip-api (documentatie: https://ip-api.com/docs/api:json).
    Acesta permite trimiterea a 45 de query-uri de geolocare pe minut.
'''

# # exemplu de request la IP info pentru a
# # obtine informatii despre localizarea unui IP
# fake_HTTP_header = {
#                     'referer': 'https://ipinfo.io/',
#                     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
#                    }
# # informatiile despre ip-ul 193.226.51.6 pe ipinfo.io
# # https://ipinfo.io/193.226.51.6 e echivalent cu
# raspuns = requests.get('https://ipinfo.io/193.226.51.6/json', headers=fake_HTTP_header)
# print (raspuns.json())
# pentru un IP rezervat retelei locale da bogon=True
# raspuns = requests.get('https://ipinfo.io/widget/10.0.0.1', headers=fake_HTTP_header)
# print (raspuns.json())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 traceroute.py <IP> <PORT>")
        exit(1)
    traceroute(sys.argv[1], int(sys.argv[2]))

    
    with open("route_output.json", "w") as f:
        json.dump(route_data, f, indent=4)
