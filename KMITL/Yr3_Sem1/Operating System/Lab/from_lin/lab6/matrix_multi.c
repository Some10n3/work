#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define M 2 // Number of rows in Matrix 1
#define N 3 // Number of columns in Matrix 1 and rows in Matrix 2
#define P 2 // Number of columns in Matrix 2

int multiplicandMatrix[M][N] = {
    {5, 6, 7},
    {4, 8, 9}
};

int multiplierMatrix[N][P] = {
    {6, 4},
    {5, 7},
    {1, 1}
};

int resultMatrix[M][P] = {0};

typedef struct {
    int row;
    int col;
} Parameters;

void* multiply(void* args) {
    Parameters* params = (Parameters*)args;
    int row = params->row;
    int col = params->col;

    resultMatrix[row][col] = 0;
    for (int i = 0; i < N; i++) {
        resultMatrix[row][col] += multiplicandMatrix[row][i] * multiplierMatrix[i][col];
    }

    free(params);
    pthread_exit(0);
}

int main() {
    pthread_t threads[M][P];
    
    // Create threads
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < P; j++) {
            Parameters* params = (Parameters*)malloc(sizeof(Parameters));
            params->row = i;
            params->col = j;
            pthread_create(&threads[i][j], NULL, multiply, (void*)params);
        }
    }

    // Join threads
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < P; j++) {
            pthread_join(threads[i][j], NULL);
        }
    }

    // Print the result matrix
    printf("Result matrix:\n");
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < P; j++) {
            printf("%d ", resultMatrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}

