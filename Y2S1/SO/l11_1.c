#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
        //ex cu bariera facuta cu variabila conditie si mutex
#define NTHRS 5

pthread_mutex_t mtx;
pthread_cond_t cond;   //variabila conditie
int arrived_count = 0; //contro pt threaduri

void barrier_point() {
    pthread_mutex_lock(&mtx); //incuiem mutex ca sa verif contorul
    arrived_count++;
    
    if (arrived_count == NTHRS) {
        pthread_cond_broadcast(&cond); //daca e ultimul, elibereaza threadurile ce asteptau sa se indepl conditia
    } else {
        //daca nu e ultimul, astepta,
        //pthread_cond_wait elibereaza mutexul temrporar si threadul asteapta semnalul lui apoi reintra
        pthread_cond_wait(&cond, &mtx);
    }
    
    pthread_mutex_unlock(&mtx);
}

void *tfun(void *v) {
    int tid = *(int *)v;
    
    printf("%d reached the barrier\n", tid);
    barrier_point();
    printf("%d passed the barrier\n", tid);
    
    free(v); //elibereaza memoria aloc pt id
    return NULL;
}

int main() {
    printf("NTHRS = %d (Variabile Conditie)\n", NTHRS);

    pthread_t threads[NTHRS];
    
    //init mutex si variabila conditie
    pthread_mutex_init(&mtx, NULL);
    pthread_cond_init(&cond, NULL);

    //init threaduri
    for (int i = 0; i < NTHRS; i++) {
        int *id = malloc(sizeof(int));
        *id = i;
        pthread_create(&threads[i], NULL, tfun, id);
    }

    //folosim join ca sa se termine (wait)
    for (int i = 0; i < NTHRS; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&mtx); //stergem astea pt a elibr esuerseel
    pthread_cond_destroy(&cond);

    return 0;
}