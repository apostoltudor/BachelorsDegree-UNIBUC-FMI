#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Eroare la socket failed");  //apeleaza socketul pt a specif protocolul
        exit(EXIT_FAILURE);
    }

    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) {
        perror("Eroare la setsockopt");
        exit(EXIT_FAILURE);  //failsafe in caz ca se opreste sv
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY; //asc pe interf locale
    address.sin_port = htons(PORT);       //host to netwoerk

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Eroare la bind");  //dau bind la socket la port
        exit(EXIT_FAILURE);
    }

    if (listen(server_fd, 3) < 0) {    //facem sv doar sa asculte conexiuni
        perror("Eroare la listen");   //arg=3=backlog, dimens max queue pt conex
        exit(EXIT_FAILURE);
    }

    printf("Serverul asculta pe portul %d...\n", PORT);

//daca accepta conex noua
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
        perror("Eroare la accept");
        exit(EXIT_FAILURE);
    }

//co,municarea sclient server, citeste sv ce da ccleintu
    int valread = read(new_socket, buffer, BUFFER_SIZE);
    printf("Am primit de la client: %s\n", buffer);

    char *hello = "Salut din partea Serverului!";
    send(new_socket, hello, strlen(hello), 0);
    printf("Mesaj de confirmare trimis.\n");

    close(new_socket);
    close(server_fd);
    return 0;
}