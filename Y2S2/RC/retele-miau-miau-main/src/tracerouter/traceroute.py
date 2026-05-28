import socket
import traceback
import time
import requests
import json
import sys

# socket - pentru crearea conexiunilor de retea
# UDP(User Datagram Protocol) este un protocol, fara conexiune, folosit pentru a trimite pachete de date
# ICMP(Internet Control Message Protocol) este un protocol de retea folosit pentru a trimite mesaje de eroare si informatii de control
# TTL(Time To Live) este un camp din antetul pachetelor IP care specifica numarul maxim de routere prin care un pachet poate trece

# Lista in care se stocheaza informatiile despre fiecare hop
route_data = []

# Functie care verifica daca un IP este dintr-un interval privat
def is_private_ip(ip):
    return ip.startswith("10.") or ip.startswith("192.168.") or (ip.startswith("172.") and 16 <= int(ip.split('.')[1]) <= 31)

# Functie care interogheaza un API pentru a obtine informatii de geolocatie despre un IP
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

# Functie principala de traceroute
def traceroute(ip, port):
    max_hops = 40
    timeout = 3
    message = b'salut'  # mesaj trimis catre destinatie
    dest_addr = socket.gethostbyname(ip)

    print(f"Traceroute catre {dest_addr}, maxim {max_hops} hop-uri:\n")

    for ttl in range(1, max_hops + 1):
        # Creaza socket UDP pentru trimiterea pachetelor
        udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
        udp_send_sock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # Creaza socket RAW pentru receptia mesajelor ICMP
        icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        icmp_recv_socket.settimeout(timeout)

        # Bind pe portul de ascultare pentru a receptiona raspunsurile ICMP
        icmp_recv_socket.bind(("", port))

        start_time = time.time()

        try:
            # Trimite mesajul UDP
            udp_send_sock.sendto(message, (dest_addr, port))
            # Asteapta raspuns ICMP
            data, addr = icmp_recv_socket.recvfrom(512)

            end_time = time.time()
            elapsed = (end_time - start_time) * 1000  # Timpul in milisecunde
            router_ip = addr[0]

            # Extrage tipul mesajului ICMP
            icmp_type = data[20]
            geo = get_geo_info(router_ip)

            # Daca tipul este 3 (Port Unreachable), inseamna ca am ajuns la destinatie
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
            # Daca tipul este 11 (Time Exceeded), routerul a respins pachetul pentru ca TTL a expirat
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

# Cod principal: se apeleaza din linia de comanda cu 2 argumente: IP si PORT
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 traceroute.py <IP> <PORT>")
        exit(1)
    
    traceroute(sys.argv[1], int(sys.argv[2]))

    # Salvare rezultat in fisier JSON
    with open("route_output.json", "w") as f:
        json.dump(route_data, f, indent=4)
