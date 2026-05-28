#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_INCREMENTS 1000000

//lab 9 ex3 de la irofti
//lab 10 efefctiv ????
// gcc lab9_ex3.c -o lab9_ex3 -pthread


int a = 0;

void *increment_function(void *arg) {
    for (int i = 0; i < NUM_INCREMENTS; i++) {
        a++;
    }  //func exec de threaduri
    return NULL;  //3 pasi, ia valoarea, incrementeaza, pune valoarea inapoi
}

int main() {
    pthread_t thread1, thread2;

    printf("Valoarea initiala a lui a: %d\n", a);
    printf("Pornesc thread-urile:\n");

    if (pthread_create(&thread1, NULL, increment_function, NULL) != 0) {
        perror("Eroare creare thread 1");
        return 1; //citeste 10, face +1, nu scrie
    }  //create
    if (pthread_create(&thread2, NULL, increment_function, NULL) != 0) {
        perror("Eroare creare thread 2");
        return 1; //inainte sa scrie primul, citeste si el gresit tot 10
    }

    pthread_join(thread1, NULL);   //wait ca sa fiu sigur ca se termina procesele
    pthread_join(thread2, NULL);

    // 3. Afișăm rezultatul final
    printf("Valoarea finala a lui a: %d\n", a);
    printf("Valoarea asteptata (teoretic): %d\n", NUM_INCREMENTS * 2);

    return 0;
}