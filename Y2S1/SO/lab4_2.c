#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

void collatz(int n) { //functia collatz
    printf("%d: ", n);
    while (n != 1) {
        printf("%d ", n);
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
    }
    printf("1.\n"); //pentru final
}

int main(int argc, char *argv[]) {
    if (argc != 2) {  //egal cu 2, nume prog, numar
        fprintf(stderr, "Usage: %s <number>\n", argv[0]); //afiseaza eroare altfel
        return 1;
    }

    int number = atoi(argv[1]); //converteste stringul in int
    pid_t pid = fork(); //se creaza un proces copil

    if (pid < 0) { //esueaza
        perror("Fork failed");
        return 1;
    } else if (pid == 0) { //totul ok
        collatz(number); //se apeleaza collatz de numar si se afiseaza
    } else {
        wait(NULL); //parintele asteapta sa se termine procesul copil
        printf("Child %d finished\n", pid);
    }

    return 0;
}
