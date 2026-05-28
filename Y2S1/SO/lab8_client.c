#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 8080

int main() {
    int sock = 0, valread;
    struct sockaddr_in serv_addr;
    char *hello = "Salut! Sunt un client C.";
    char buffer[1024] = {0};

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {  //creez socket
        printf("\n Eroare la creare socket \n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        printf("\nAdresa invalida / Address not supported \n");
        return -1;  //fac adresa din text in binar cu presentation to network
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("\nConexiunea a esuat \n");
        return -1;  //initiez 3 way hadnshake
    }

    send(sock, hello, strlen(hello), 0);
    printf("Mesaj trimis catre server.\n");

    valread = read(sock, buffer, 1024);
    printf("Raspuns de la server: %s\n", buffer);

    close(sock);
    return 0;
}