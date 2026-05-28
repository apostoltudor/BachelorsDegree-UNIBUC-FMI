#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
//lab 7
#define FIFO1 "/tmp/fifo_a_to_b"
#define FIFO2 "/tmp/fifo_b_to_a"

int main() {
    printf("B: Ma conectez...\n");
    
    int fd_read = open(FIFO1, O_RDONLY);
    if (fd_read < 0) { perror("open fifo1"); return 1; }
    
    int fd_write = open(FIFO2, O_WRONLY);
    if (fd_write < 0) { perror("open fifo2"); return 1; }
    
    printf("B: Conectat!\n");
    
    char buf[100];

    while (1) {
        read(fd_read, buf, sizeof(buf));
        printf("A: %s", buf);

        printf("B: ");
        fflush(stdout);
        fgets(buf, sizeof(buf), stdin);
        write(fd_write, buf, strlen(buf) + 1);
    }

    close(fd_read);
    close(fd_write);
    return 0;
}
