#include <unistd.h>

int main() {
    const char *message = "Hello, World!\n";
    write(1, message, 14); // 1 e file descriptor pt stdout
    return 0;
}