#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork(); //se creaza un proces copil

    if (pid < 0) //esueaza
        return 1 ;
      else if (pid == 0) { //totul ok
        char *argv[] = {"/bin/ls", NULL};
        execve("/bin/ls", argv, NULL); //foloseste ls ca sa listeze fisierele din directorul curent
        perror(NULL);
    } else {
        printf("My PID = %d, Child PID = %d\n", getpid(), pid); //afiseaza pid la parinte si copil
        wait(NULL);  //ca sa fie terminat procesul copil inainte de parinte
        printf("Child %d finished\n", pid);
    }
    return 0;
}
