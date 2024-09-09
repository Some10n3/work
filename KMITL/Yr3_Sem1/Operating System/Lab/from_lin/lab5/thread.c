#include <stdio.h>
#include <pthread.h>

int child_result = 0;

void* child_thread(void* arg) {
    int number = *((int*)arg);
    for (int i = 1; i <= 2 * number; i++) {
        child_result += i;
    }
    pthread_exit(0);
}

int main() {
    int number;
    int parent_result = 0;

    printf("Enter a number: ");
    scanf("%d", &number);

    for (int i = 1; i <= number; i++) {
        parent_result += i;
    }

    pthread_t tid;
    pthread_create(&tid, NULL, child_thread, &number);
    pthread_join(tid, NULL);

    int final_result = parent_result + child_result;
    printf("Final result: %d\n", final_result);

    return 0;
}

