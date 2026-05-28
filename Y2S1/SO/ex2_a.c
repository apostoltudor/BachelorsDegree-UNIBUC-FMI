#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/stat.h>
#include <errno.h>
//lab 7
#define FIFO1 "/tmp/fifo_a_to_b"
#define FIFO2 "/tmp/fifo_b_to_a"

int main() {
    unlink(FIFO1);
    unlink(FIFO2);
    
    if (mkfifo(FIFO1, 0666) < 0) {
        perror("mkfifo fifo_a_to_b");
        return 1;
    }
    if (mkfifo(FIFO2, 0666) < 0) {
        perror("mkfifo fifo_b_to_a");
        return 1;
    }
    
    printf("A: FIFO-uri create in /tmp/. Astept B...\n");
    
    int fd_write = open(FIFO1, O_WRONLY);
    if (fd_write < 0) { perror("open"); return 1; }
    
    int fd_read = open(FIFO2, O_RDONLY);
    if (fd_read < 0) { perror("open"); return 1; }
    
    printf("A: Conectat!\n");
    
    char buf[100];

    while (1) {
        printf("A: ");
        fflush(stdout);
        fgets(buf, sizeof(buf), stdin);
        write(fd_write, buf, strlen(buf) + 1);

        read(fd_read, buf, sizeof(buf));
        printf("B: %s", buf);
    }

    close(fd_write);
    close(fd_read);
    return 0;
}
