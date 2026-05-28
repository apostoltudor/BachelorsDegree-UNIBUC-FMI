#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
// lab 7
int main(int argc, char *argv[]) {
    int fd[2];
    pipe(fd);

    if (fork() == 0) {
        // Copil: citeste numerele si calculeaza suma
        close(fd[1]);

        int n, sum = 0, x;
        read(fd[0], &n, sizeof(n));
        for (int i = 0; i < n; i++) {
            read(fd[0], &x, sizeof(x));
            sum += x;
        }
        printf("Suma: %d\n", sum);
        close(fd[0]);
    } else {
        // Parinte: trimite numerele
        close(fd[0]);

        int n = argc - 1;
        write(fd[1], &n, sizeof(n));
        for (int i = 1; i < argc; i++) {
            int num = atoi(argv[i]);
            write(fd[1], &num, sizeof(num));
        }
        close(fd[1]);
    }

    return 0;
}
