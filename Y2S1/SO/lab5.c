#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <string.h>
//lab6
#define SHM_NAME "/collatz_shm"
#define MAX_NUMBERS 10
#define MAX_LENGTH 100

void collatz_sequence(int n, char *result) {
    char buffer[10];
    while (n != 1) {
        sprintf(buffer, "%d ", n);
        strcat(result, buffer);
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
    }
    strcat(result, "1."); //adauga 1 la final
}

int main(int argc, char *argv[]) {
    if (argc < 2) { //minim 2 arg, numele prog si macar un numar
        fprintf(stderr, "usage: %s num1 num2 ...\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int num_count = argc - 1;  //nr de numere, se scade numele prog
    int shm_fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666); //deschide zona de memorie partajata
    ftruncate(shm_fd, num_count * MAX_LENGTH); //seteaza lungimea zonei de memorie partajata
    char *shm_base = mmap(0, num_count * MAX_LENGTH, PROT_WRITE, MAP_SHARED, shm_fd, 0); //mapeaza zona de memorie partajata

        printf("starting parent %d\n", getpid());

    for (int i = 0; i < num_count; i++) { //creeaza procese copil pt fiecare numar
        pid_t pid = fork();
        if (pid == 0) {  //totul ok
            char *shm_ptr = shm_base + i * MAX_LENGTH;
            int num = atoi(argv[i + 1]);  //face din string int numerele
            collatz_sequence(num, shm_ptr); //executa collatz pt fiecare numar
            printf("done parent %d me %d\n", getppid(), getpid()); //afiseaza process id pentru parinte si copil
            exit(EXIT_SUCCESS);
        }
    }

    for (int i = 0; i < num_count; i++) {
        wait(NULL);  //parintele asteapta fiecare copil
    }

    for (int i = 0; i < num_count; i++) {
        printf("%s: %s\n", argv[i + 1], shm_base + i * MAX_LENGTH); //afiseaza rezultatele
    }

    munmap(shm_base, num_count * MAX_LENGTH); //goleste zona de memorie partajata
    shm_unlink(SHM_NAME); //apoi o sterge

    return 0;
}