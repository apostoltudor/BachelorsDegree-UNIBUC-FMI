FROM snisioi/retele:2021
# tracerouter
# RUN apt-get update && apt-get install -y iptables iproute2 libnetfilter-queue-dev whois

# RUN pip3 install --upgrade python-iptables cython requests

# RUN mkdir -p /scripts
# COPY src/tracerouter/*.sh /scripts/

# RUN mkdir -p /src
# COPY src/tracerouter/*.py /src/


# dns blocker

RUN apt-get update && apt-get install -y python3-pip \ 
        iptables netfilter-persistent
RUN pip3 install --no-cache-dir matplotlib dnslib \ 
        dnspython

WORKDIR /app

COPY ./src/dns_blocker/ /app/

RUN mkdir -p /app/files

COPY ./src/dns_blocker/files/ /app/files/

COPY scripts/ /scripts/ 
RUN chmod +x /scripts/*.sh 

CMD ["bash", "-c", "/scripts/setup_iptables.sh && python3 /app/dns_blocker.py"]