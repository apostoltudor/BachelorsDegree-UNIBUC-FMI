#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 1024  //fol la coppiere

int main(int argc, char *argv[]) {
    if (argc != 3) {   //trb sa fie egal cu 3, nume prog, sursa, destinatie
        fprintf(stderr, "usage: %s source_file destination_file\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int src_fd = open(argv[1], O_RDONLY); //citeste ce e in sursa
    if (src_fd < 0) { //eroare daca file descriptor e negativ
        perror("open source");
        exit(EXIT_FAILURE);
    }

    int dest_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644); 
    //transcrie in fisierul destinatie si il creeaza daca nu exista
    if (dest_fd < 0) { //lfl ca mai sus
        perror("open destination");
        close(src_fd); //inchide fisierulsursa
        exit(EXIT_FAILURE);
    }

    char buffer[BUFFER_SIZE]; //unde sa se copieze temporar datele din sursa
    ssize_t bytes_read, bytes_written;

    while ((bytes_read = read(src_fd, buffer, BUFFER_SIZE)) > 0) { //citeste
        bytes_written = write(dest_fd, buffer, bytes_read); //scrie
        if (bytes_written != bytes_read) { //verif daca e copiat bine
            perror("write");
            close(src_fd);
            close(dest_fd);
            exit(EXIT_FAILURE);
        }
    }

    if (bytes_read < 0) { //verif daca s-a realizat corect citirea
        perror("read");
    }

    close(src_fd);
    close(dest_fd);

    return 0;
}