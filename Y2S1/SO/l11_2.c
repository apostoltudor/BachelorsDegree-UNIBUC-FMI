#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
    //aici e ex cu reader-writer lock in loc de mutex normal
    //unde avem unii de sunt sciitori si unii de sunt cititori
#define NUM_READERS 5
#define NUM_WRITERS 2
//variabila partajata
int shared_data = 0;
//rwlock, citeste oricine, scrie doar unul
//aici daca vin cititori noi incontinuu, sciitori asteapta la infinit
pthread_rwlock_t rwlock;

void *writer_func(void *arg) {
    int id = *(int *)arg;
    free(arg); //elib mem alocata pentru id

    //cn scrie are nevoie de acces exclusiv si dam lock de scriere
    pthread_rwlock_wrlock(&rwlock); 
    
    shared_data++; //modif datele
    printf("Writer %d: a scris valoarea %d\n", id, shared_data);
    sleep(3); //simulam scrierea si blocarea celorlalte threaduri

    pthread_rwlock_unlock(&rwlock); //deschidem dupa ce a term de scris
    return NULL;
}

void *reader_func(void *arg) {
    int id = *(int *)arg;
    free(arg); //elib mem alocata pentru id

    //aici pot citi mai multi odata si dam lock de citire
    pthread_rwlock_rdlock(&rwlock); 
    
    //pot intra mai multi care citesc, da nu sa si scrie
    printf("Reader %d: a citit valoarea %d\n", id, shared_data);
    sleep(1); //simulam citirea

    pthread_rwlock_unlock(&rwlock); //deblocam 
    return NULL;
}

int main() {
    pthread_t readers[NUM_READERS];
    pthread_t writers[NUM_WRITERS];

    //init rwlock, null pt setari default
    if (pthread_rwlock_init(&rwlock, NULL) != 0) {
        perror("Eroare la init rwlock");
        return 1;
    }

    //init threadurile si le dam un id si apelam functia de write
    for (int i = 0; i < NUM_WRITERS; i++) {
        int *id = malloc(sizeof(int));
        *id = i;
        if (pthread_create(&writers[i], NULL, writer_func, id) != 0) {
            perror("Eroare creare writer");
            return 1;
        }
    }

    //lfl dar cu read
    for (int i = 0; i < NUM_READERS; i++) {
        int *id = malloc(sizeof(int));
        *id = i;
        if (pthread_create(&readers[i], NULL, reader_func, id) != 0) {
            perror("Eroare creare reader");
            return 1;
        }
    }

    //ast sa termine toti cu join (wait)
    for (int i = 0; i < NUM_WRITERS; i++) {
        pthread_join(writers[i], NULL);
    }
    for (int i = 0; i < NUM_READERS; i++) {
        pthread_join(readers[i], NULL);
    }

    //stergem rwlock-ul pt a elibera memoria
    pthread_rwlock_destroy(&rwlock);

    return 0;
}