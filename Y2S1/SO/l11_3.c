#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
        //rwlock pt unde scriitori au prioritate fata de cititori fara sa ii blocheze pe term lung
#define NUM_READERS 5
#define NUM_WRITERS 2

int shared_data = 0;

typedef struct {  //definim structura pt a vedea si cati scriitori asteapta
    pthread_mutex_t mtx;
    pthread_cond_t can_read;
    pthread_cond_t can_write;
    int readers_active;  //cati sunt cititori activi
    int writer_active;   //daca e un scriitor activ
    int writers_waiting; //cati scriitori asteapta
} rw_lock_t;

rw_lock_t rwlock; //o declram global

void init_rwlock(rw_lock_t *l) {
    pthread_mutex_init(&l->mtx, NULL);
    pthread_cond_init(&l->can_read, NULL);
    pthread_cond_init(&l->can_write, NULL);
    l->readers_active = 0;
    l->writer_active = 0;
    l->writers_waiting = 0;  //init strcutului
}

void my_read_lock(rw_lock_t *l) {
    pthread_mutex_lock(&l->mtx);
    //daca cnv scrie sau cineva ast sa scrie, se pune cititorul in coada dupa el
    while (l->writer_active || l->writers_waiting > 0) {
        pthread_cond_wait(&l->can_read, &l->mtx);
    }
    l->readers_active++;
    pthread_mutex_unlock(&l->mtx);
}

void my_read_unlock(rw_lock_t *l) {
    pthread_mutex_lock(&l->mtx);
    l->readers_active--;
    //daca sunt ultimul cititor si sunt scriitori care ast, ii trezesc
    if (l->readers_active == 0) {
        pthread_cond_signal(&l->can_write); //dam semnalul sa se scrie
    }
    pthread_mutex_unlock(&l->mtx);
}

void my_write_lock(rw_lock_t *l) {
    pthread_mutex_lock(&l->mtx);
    l->writers_waiting++; //adaug scriitor in coada
    
    //cat timp exista cititori activi sau un scriitor activ, astept
    while (l->readers_active > 0 || l->writer_active) {
        pthread_cond_wait(&l->can_write, &l->mtx);
    }
    
    l->writers_waiting--; //iesim din coada
    l->writer_active = 1; //scriem activ
    pthread_mutex_unlock(&l->mtx);
}

void my_write_unlock(rw_lock_t *l) {
    pthread_mutex_lock(&l->mtx);
    l->writer_active = 0;
    
    //daca mai sunt scriitori, ii las pe ei, daca nu, las cititorii
    if (l->writers_waiting > 0) {
        pthread_cond_signal(&l->can_write); //semnal daca mai sunt scriitori
    } else {  //signal trezeste minim unul, broadcast pe toti
        pthread_cond_broadcast(&l->can_read); //broadcast pt TOTI cititori
    }
    pthread_mutex_unlock(&l->mtx);
}

void *writer_func(void *arg) {
    int id = *(int *)arg;
    free(arg);  //elib mem alocata pentru id

    //simuleaza un sctiiror care scrie de 3 ori
    for (int i = 0; i < 3; i++) {
        usleep(rand() % 100000); //punem un delay random ca sa facem 
                                 //mecanismul de prioritate sa intervina
        my_write_lock(&rwlock);
        shared_data = id; //sciitorul isi scrie id-ul
        printf("[Writer %d] A scris valoarea %d (Writers waiting: %d)\n", 
               id, shared_data, rwlock.writers_waiting);
        
        my_write_unlock(&rwlock);
    }
    return NULL;
}

void *reader_func(void *arg) {
    int id = *(int *)arg;
    free(arg); //elib mem alocata pentru id

    for (int i = 0; i < 3; i++) {
        usleep(rand() % 100000);  //lfl ca mai devreme
        my_read_lock(&rwlock);
        printf("  (Reader %d) A citit valoarea %d\n", id, shared_data);
        my_read_unlock(&rwlock);
    }
    return NULL;
}

int main() {
    pthread_t readers[NUM_READERS];
    pthread_t writers[NUM_WRITERS];
    srand(time(NULL)); //seed pt alg de rand

    init_rwlock(&rwlock);

    //init threaduri
    for (int i = 0; i < NUM_WRITERS; i++) {
        int *id = malloc(sizeof(int)); *id = i + 100; //scriitorii cu id-uri >100
        pthread_create(&writers[i], NULL, writer_func, id);
    }
    for (int i = 0; i < NUM_READERS; i++) {
        int *id = malloc(sizeof(int)); *id = i;
        pthread_create(&readers[i], NULL, reader_func, id);
    }

    //join ca sa se termine (wait)
    for (int i = 0; i < NUM_WRITERS; i++) pthread_join(writers[i], NULL);
    for (int i = 0; i < NUM_READERS; i++) pthread_join(readers[i], NULL);

    //stergem mutex si variabile de conditie din rwlock ca sa eliberam
    pthread_mutex_destroy(&rwlock.mtx);
    pthread_cond_destroy(&rwlock.can_read);
    pthread_cond_destroy(&rwlock.can_write);

    return 0;
}