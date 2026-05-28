#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
        //problema cu unde fiecare thread foloseste reusese si ne folosim de mutex 
        //ca sa nu se duca una peste alta si sa ia resurse pe rand
#define MAX_RESOURCES 5

//lab 10 ex 1 la irofti

//lab 11 in sapt 11 adica aia cu craciunul. (saptamana -1)
int available_resources = MAX_RESOURCES;
pthread_mutex_t resource_mutex; //obj

int decrease_count(int count) { //scade nr de resurse valabile si folosim referinta pt a proteja de racce condition
    pthread_mutex_lock(&resource_mutex); //odata ce a intrat in mutex, il incuie ca sa nu se citeasca simultan
    if (available_resources < count) {   //daca nu mai sunt resurse, trb sa descuiem 
        pthread_mutex_unlock(&resource_mutex);  //daca nu eliberam ne blocam si apare deadlock
        return -1;
    } else {
        available_resources -= count;
        printf("got %d resources %d remaining\n", count, available_resources); //nr obtinut si ramas
        pthread_mutex_unlock(&resource_mutex); //iese si elibereaza cutia
        return 0;
    }
}

int increase_count(int count) {  
    pthread_mutex_lock(&resource_mutex);   //intra si inchide cutia pt a nu se citi simultan
    available_resources += count;
    printf("released %d resources %d remaining\n", count, available_resources); //nr eliberat si ramas
    pthread_mutex_unlock(&resource_mutex); //iese si deschide cutia
    return 0;
}

void* resource_user(void* arg) { //fiecare thread cu resursele lui
    int count = *(int*)arg;  //pune in count
    if (decrease_count(count) == 0) { //daca e 0 a avut de unde sa ia resuerse 
        //folosirea resurselor
        increase_count(count); //returneaza resursele dupa ce completeaza actiunea
    } //daca descrease e -1, nu face nimic neavand resurse
    return NULL; 
}

int main() {
    pthread_t threads[5]; //5 threaduri
    int resource_requests[5] = {2, 2, 1, 3, 2};  //nr de resurse pt fiecare thread

    pthread_mutex_init(&resource_mutex, NULL); //genereaza mutex-ul

    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, resource_user, &resource_requests[i]); //generam thread si ii zicem sa exec resource user cu arg din res req
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL); //asteapta thread-ul sa termine ca sa func corect programul
    }

    pthread_mutex_destroy(&resource_mutex);  //sterge mutex-ul ca sa elibereze memoria

    return 0;
}


















//scheduler / planificator