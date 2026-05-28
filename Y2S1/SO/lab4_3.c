#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

void collatz(int n) {
    printf("%d: ", n);
    while (n != 1) {
        printf("%d ", n);
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
    }
    printf("1.\n"); //pt final
}

int main(int argc, char *argv[]) {
    if (argc < 2) { //trb sa fie macar doua argumente, nume prog si macar un numar
        fprintf(stderr, "Usage: %s <numbers...>\n", argv[0]); //eroare daca nu
        return 1;
    }

    printf("Starting parent %d\n", getpid());
    
    for (int i = 1; i < argc; i++) {
        int number = atoi(argv[i]); //se fac numerele din string in int
        pid_t pid = fork(); //proces copil

        if (pid < 0) {
            perror("Fork failed");
            return 1;
        } else if (pid == 0) { //pid copil=0 adica e ok
            collatz(number); //apeleaza collatz pt numar
            printf("Done Parent %d Me %d\n", getppid(), getpid());
            exit(0);
        }
    }

    for (int i = 1; i < argc; i++) {
        wait(NULL);  //parintele asteapta sa se termine procesul copil pt fiecare numar
    }

    return 0;
}
