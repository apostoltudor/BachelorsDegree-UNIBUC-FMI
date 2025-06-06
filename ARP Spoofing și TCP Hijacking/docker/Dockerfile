FROM snisioi/retele:2021
# tracerouter
#RUN apt-get update && apt-get install -y iptables iproute2 libnetfilter-queue-dev whois
#
#RUN pip3 install --upgrade python-iptables cython requests
#
#RUN mkdir -p /scripts
#COPY src/tracerouter/*.sh /scripts/
#
#RUN mkdir -p /src
#COPY src/tracerouter/*.py /src/
#

# dns blocker

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --no-cache-dir matplotlib dnslib

WORKDIR /app
COPY ./src/dns_blocker/ /app/

CMD ["python3", "dns_blocker.py"]

#ARP Spoofing
COPY src/middle.sh /src/middle.sh
COPY src/router.sh /src/router.sh
COPY src/client.sh /src/client.sh

RUN chmod +x /src/*.sh


