#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define MAX 10 
//struct defineste clar si cclarifica ce date va folosi fiecare thread
//lab9 ex 2 de la irofti

//lab 9 teoretic????
typedef struct {
    int row; //c
    int col;
    int p;
    int (*A)[MAX];
    int (*B)[MAX];
    int (*C)[MAX];
} ThreadData;  //struct-ul care stocheaza datele necesare pt fiecare thread   

void *calcul_element(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    int sum = 0;
    for (int k = 0; k < data->p; k++) {  //row A * col B
        sum += data->A[data->row][k] * data->B[k][data->col];
    }
    data->C[data->row][data->col] = sum; //punem in C rez
    pthread_exit(0);
}

int main() {
    int m, p, n;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    printf("introduceti dimensiunile matricelor A si B (m p n): ");
    scanf("%d %d %d", &m, &p, &n);

    printf("introduceti elementele matricei A:\n");
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("introduceti elementele matricei B:\n");
    for (int i = 0; i < p; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    pthread_t threads[MAX][MAX];
    ThreadData data[MAX][MAX];  //decl thread-urile si datele din struct necesare pt matricea rezultat C

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            data[i][j].row = i;
            data[i][j].col = j;
            data[i][j].p = p;
            data[i][j].A = A;
            data[i][j].B = B;
            data[i][j].C = C;
            pthread_create(&threads[i][j], NULL, calcul_element, &data[i][j]);
        }
    }  // se init datele pt fiecare elem din matr C si se creeaza un thread pt a calc fiecare elem

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            pthread_join(threads[i][j], NULL);
        }   //wait
    }  //thread-ul pt pozitia i,j calculeaza valoarea in C

    printf("matricea rezultata C:\n");
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}
