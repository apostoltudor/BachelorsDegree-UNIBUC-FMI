 #include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_THREADS 5 //spunem nr de threaduri care trb sa se soncrionizeze

pthread_barrier_t barrier; //glbl
pthread_mutex_t mtx; //mutex opt a afisa bn la print

void *thread_routine(void *arg) {
int id = *(int *)arg; //luam id-ul de la thread

printf("thread %d a inceput executia\n", id);


pthread_mutex_lock(&mtx);
printf("thread-ul %d a ajuns la bariera. Asteapta celelalte thread-uri.\n", id);
pthread_mutex_unlock(&mtx);

//cand ultimu thread apeleaza wait, bariera nu mai e si continua toti
pthread_barrier_wait(&barrier);

printf("thread-ul %d a trecut de bariera\n", id);
free(arg); //elib mem alocata pt id-ul asta
return NULL;
}

int main() {
pthread_t threads[NUM_THREADS];
pthread_mutex_init(&mtx, NULL);

if (pthread_barrier_init(&barrier, NULL, NUM_THREADS) != 0) {
perror("Eroare la initializarea barierei");
return 1;
}

printf("incepe crearea a %d thread-uri\n", NUM_THREADS);

for (int i = 0; i < NUM_THREADS; i++) {
int *id = malloc(sizeof(int)); //aloc mem pt id-ul thread-ului
*id = i;
if (pthread_create(&threads[i], NULL, thread_routine, id) != 0) {
perror("Eroare la crearea thread-ului");
return 1;
}
}

//wait
for (int i = 0; i < NUM_THREADS; i++) {
pthread_join(threads[i], NULL);
}

printf("toate thread-urile au trminat\n");

//distrugem bariera si mutex-ul pt a elibera resursele
pthread_barrier_destroy(&barrier);
pthread_mutex_destroy(&mtx);

return 0;
}