# Traceroute - Analiza Locatii IP din Regiuni Diferite

Acest raport documenteaza locatiile IP prin care trece traficul de retea catre site-uri din diverse regiuni geografice: **Asia (.cn)**, **Africa (.za)** si **Australia (.au)**. Informatiile sunt obtinute prin scriptul personalizat `run_traceroute.sh`, care foloseste un serviciu de geolocatie IP.

---

## 🔹 Test 1: China (.cn)

**Domeniu testat:** www.fudan.edu.cn
**IP rezolvat:** `202.120.224.81`  
**Port:** `33434`  

Pornesc traceroute catre 202.120.224.81:33434...
Traceroute catre 202.120.224.81, maxim 40 hop-uri:

| TTL | Adresa IP         | Timp (ms) | Locatie Geografica                            |
|-----|-------------------|-----------|-----------------------------------------------|
| 1   | 172.29.208.1      | 0.69      | No geo info                                   |
| 2   | 192.168.1.1       | 2.8       | No geo info                                   |
| 3   | 10.0.0.1          | 3.17      | No geo info                                   |
| 4   | 10.30.2.145       | 3.9       | No geo info                                   |
| 5   | 10.220.164.130    | 6.44      | No geo info                                   |
| 6   | * * *             | Timeout   | -                                             |
| 7   | * * *             | Timeout   | -                                             |
| 8   | 154.54.38.245     | 19.7      | Romania, București, Bucharest                 |
| 9   | 154.54.59.177     | 20.53     | Hungary, Budapest, Budapest                   |
| 10  | 154.54.59.185     | 23.26     | Slovakia, Bratislava Region, Bratislava       |
| 11  | 154.54.59.182     | 30.34     | Germany, Bavaria, Munich                      |
| 12  | 154.54.62.121     | 28.83     | Germany, Bavaria, Munich                      |
| 13  | 154.54.72.117     | 45.59     | United States, District of Columbia, Washington |
| 14  | 154.54.47.165     | 117.44    | France, Île-de-France, Paris                  |
| 15  | 154.54.171.66     | 118.77    | United States, District of Columbia, Washington |
| 16  | 154.54.7.158      | 136.69    | United States, Georgia, Atlanta               |
| 17  | 154.54.29.134     | 141.69    | United States, Mississippi, Jackson           |
| 18  | 154.54.41.53      | 151.81    | United States, Mississippi, Jackson           |
| 19  | 154.54.165.30     | 160.59    | United States, Texas, Dallas                  |
| 20  | 154.54.166.70     | 169.11    | United States, California, Stockton           |
| 21  | 154.54.45.162     | 177.67    | United States, California, Los Angeles        |
| 22  | 154.54.42.102     | 179.24    | United States, California, Los Angeles        |
| 23  | 38.88.196.186     | 179.0     | United States, California, Los Angeles        |
| 24  | 101.4.117.169     | 327.58    | China, Beijing, Haidian                       |
| 25  | 101.4.114.169     | 323.41    | China, Beijing, Haidian                       |
| 26  | 101.4.118.41      | 326.1     | China, Beijing, Haidian                       |
| 27  | 101.4.115.202     | 349.92    | China, Beijing, Haidian                       |
| 28  | * * *             | Timeout   | -                                             |
| 29  | 202.112.27.18     | 357.29    | China, Beijing, Beijing                       |
| 30  | 10.255.38.249     | 349.59    | No geo info                                   |
| 31  | 10.255.249.46     | 349.64    | No geo info                                   |
| 32  | 10.255.19.11      | 348.6     | No geo info                                   |
| 33  | 10.250.2.100      | 349.91    | No geo info                                   |
| 34  | 10.250.2.162      | 351.34    | No geo info                                   |
| 35  | 202.120.224.81    | 349.66    | China, Shanghai, Shanghai (DESTINATION REACHED) |


---

## 🔹 Test 2: Africa de Sud (.za)
**Domeniu testat:** www.gov.za
**IP destinatie:** `197.103.130.130`  
**Port:** `33434`  

Pornesc traceroute catre 197.103.130.130:33434...
Traceroute catre 197.103.130.130, maxim 30 hop-uri:

| TTL | Adresa IP         | Timp (ms) | Locatie Geografica                   |
|-----|-------------------|-----------|--------------------------------------|
| 1   | 172.29.208.1      | 0.75      | No geo info                          |
| 2   | 192.168.1.1       | 2.75      | No geo info                          |
| 3   | 10.0.0.1          | 3.41      | No geo info                          |
| 4   | 172.19.212.81     | 3.71      | No geo info                          |
| 5   | 10.220.164.128    | 3.90      | No geo info                          |
| 6   | * * *             | Timeout   | -                                    |
| 7   | 10.221.96.25      | 47.59     | No geo info                          |
| 8   | 195.66.224.198    | 46.06     | United Kingdom, England, London      |
| 9   | 168.209.100.213   | 221.54    | South Africa, Gauteng, Johannesburg  |
| 10  | 168.209.1.200     | 218.91    | South Africa, Gauteng, Johannesburg  |
| 11  | 168.209.129.138   | 211.52    | South Africa, Gauteng, Johannesburg  |
| 12  | 168.209.90.94     | 213.91    | South Africa, Gauteng, Johannesburg  |
| 13  | 168.209.131.145   | 210.72    | South Africa, Gauteng, Johannesburg  |
| 14  | 197.103.130.130   | 218.22    | South Africa, Gauteng, Johannesburg (DESTINATION REACHED) |

---

## 🔹 Test 3: Australia (.au)

**Domeniu testat:** https://www.une.edu.au/  
**IP rezolvat:** `2.58.104.11`  
**Port:** `33434`  

Pornesc traceroute catre 2.58.104.11:33434...
Traceroute catre 2.58.104.11, maxim 30 hop-uri:

| TTL | Adresa IP       | Timp (ms) | Locatie Geografica                  |
|-----|-----------------|-----------|-------------------------------------|
| 1   | 172.29.208.1    | 0.54      | No geo info                         |
| 2   | 192.168.1.1     | 2.06      | No geo info                         |
| 3   | 10.0.0.1        | 4.78      | No geo info                         |
| 4   | 172.19.212.81   | 7.04      | No geo info                         |
| 5   | 10.220.164.128  | 4.22      | No geo info                         |
| 6   | 10.221.100.92   | 5.01      | No geo info                         |
| 7   | 86.120.70.185   | 6.09      | Romania, Botoșani County, Botoșani  |
| 8   | 162.158.16.13   | 6.50      | Romania, Bucharest, Bucharest        |
| 9   | 2.58.104.11     | 8.00      | Australia, New South Wales, Sydney (DESTINATION REACHED) |


---

## Rulare

1. Deschide terminalul în WSL (Windows Subsystem for Linux).  
2. Navighează în directorul proiectului: retele-miau-miau/src/tracerouter  
3. Construiește imaginea Docker: docker compose build  
4. Pornește containerul în fundal: docker compose up -d  
5. Rulează scriptul pentru traceroute: ./run_traceroute.sh  
6. Așteaptă afișarea rezultatelor în terminal.  
7. Pentru a opri containerul Docker: docker compose down  
