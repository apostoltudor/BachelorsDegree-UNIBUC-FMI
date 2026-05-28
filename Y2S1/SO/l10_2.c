
//lab 10 ex 2 la irofti

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
    //problema cu bariera facuta din semafor si mutex
#define NTHRS 5

pthread_mutex_t mtx;
sem_t sem;
int arrived_count = 0; //contor pt cate thread-uri au ajuns la bariera

void barrier_point() {
    pthread_mutex_lock(&mtx); //oprim accesul pt ca incrementam contorul
    arrived_count++;
    
    if (arrived_count == NTHRS) {
        pthread_mutex_unlock(&mtx); //daca au aj toate eliberam mutexul
        //si daca esti ultimul le deblochezi pe toate celelalte de la semafor cu post
        for (int i = 0; i < NTHRS - 1; i++) {
            sem_post(&sem);
        }
    } else {
        //daca nu au ajuns toate
        pthread_mutex_unlock(&mtx); //eliberam mutextul ca sa poate veni si alte threaduri
        
        sem_wait(&sem); //le facem sa astepte la semafor cu wait (aici e bariera)
    }
}

void *tfun(void *v) {
    int tid = *(int *)v;
    
    printf("%d reached the barrier\n", tid);
    barrier_point(); //asteapta sa ajunga toate aici
    printf("%d passed the barrier\n", tid);
    
    free(v); // Eliberăm memoria alocată pentru ID
    return NULL;
}

int main() {
    printf("NTHRS = %d\n", NTHRS); //nr de threads

    pthread_t threads[NTHRS];
    
    if (pthread_mutex_init(&mtx, NULL) != 0) {
        perror("mutex init"); return 1; //facem un mutex
    }
    if (sem_init(&sem, 0, 0) != 0) { //init semafor blocat cu 0 si pt toate threadurile
        perror("sem init"); return 1;
    }

    for (int i = 0; i < NTHRS; i++) { //init threaduri si sa apeleze tfun
        int *id = malloc(sizeof(int));
        *id = i; //alocam memorie pt id si ii dam o valoare
        if (pthread_create(&threads[i], NULL, tfun, id) != 0) {
            perror("thread create"); return 1;
        }
    }

    for (int i = 0; i < NTHRS; i++) {
        pthread_join(threads[i], NULL);
    }   //asteptam sa se termine toate cu join (wait)

    pthread_mutex_destroy(&mtx);  //stergem mutex si semafor ca sa elib resursele
    sem_destroy(&sem);

    return 0;
}