#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
//lab 9 ex 1 de la irofti


//lab 8 teoretic???? 
char *rev_cuv; //decl pointer global
char *cuv;

void *reverse(void *arg)
{
    int cuv_lungime = strlen(cuv) - 1; //lungimea stringului fara term de sir
    for (int i = cuv_lungime; i >= 0; i--) //o ia de la coada la cap
        rev_cuv[cuv_lungime - i] = cuv[i]; //copiaza alea in ordinea de mai sus
    pthread_exit(NULL);
}

int main(int argc, char **argv) // p la p
{
    cuv = argv[1];

    rev_cuv = malloc(strlen(cuv) * sizeof(char)); //memory alloc

    pthread_t tid_rev; //thread indentifier
    pthread_create(&tid_rev, NULL, reverse, NULL); //nu trim nimic
    pthread_join(tid_rev, NULL); //ast sa ternine, un wait

    printf("%s\n", rev_cuv);
    return 0;
}