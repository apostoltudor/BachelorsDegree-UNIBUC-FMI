# TCP Server
import socket
import logging
import time

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

port = 10000
adresa = '0.0.0.0'
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portul %d", adresa, port)
sock.listen(5)

try:
    while True:
        logging.info('Asteptam conexiuni...')
        conexiune, address = sock.accept()
        logging.info("Handshake cu %s", address)
        try:
            while True:
                data = conexiune.recv(1024)
                if not data:
                    break
                logging.info('Content primit: "%s"', data)
                conexiune.send(b"Server a primit mesajul: " + data)
                time.sleep(3)
        except Exception as e:
            logging.info(f'Eroare conexiune: {e}')
        finally:
            conexiune.close()
except KeyboardInterrupt:
    logging.info('Server oprit de utilizator.')

finally:
    sock.close()
