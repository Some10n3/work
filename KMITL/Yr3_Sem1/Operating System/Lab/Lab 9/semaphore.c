#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5  // Size of the bounded buffer
#define ROUNDS 40      // Number of rounds for producer and consumer

int buffer[BUFFER_SIZE];  // Shared buffer
int in = 0;               // Index for the producer to insert items
int out = 0;              // Index for the consumer to remove items
int count = 0;            // Track number of items in the buffer

// Semaphores
sem_t empty;  // Semaphore to count empty slots
sem_t full;   // Semaphore to count full slots
sem_t mutex;  // Semaphore to enforce mutual exclusion

void *insertbuffer(void *arg) {
    for (int i = 0; i <= ROUNDS; i++) {
        // Produce an item (e.g., item 0, 1, 2, ...)
        int item = i;

        // Wait until there's an empty slot
        sem_wait(&empty);

        // Lock the buffer (critical section)
        sem_wait(&mutex);

        // Insert the item into the buffer
        buffer[in] = item;
        count++;
        printf("Producer entered: %d Buffer size = %d\n", item, count);
        in = (in + 1) % BUFFER_SIZE;

        // Unlock the buffer
        sem_post(&mutex);

        // Signal that there's a full slot
        sem_post(&full);

        // If the buffer is full, show that the producer is waiting
        if (count == BUFFER_SIZE) {
            printf("Producer: Buffer Full\n");
        }

        sleep(1);  // Simulate work
    }
    return NULL;
}

void *readbuffer(void *arg) {
    for (int i = 0; i <= ROUNDS; i++) {
        // Wait until the buffer has at least one item
        sem_wait(&full);

        // Lock the buffer (critical section)
        sem_wait(&mutex);

        // Remove the item from the buffer
        int item = buffer[out];
        count--;
        printf("Consumer consumed: %d Buffer size = %d\n", item, count);
        out = (out + 1) % BUFFER_SIZE;

        // Unlock the buffer
        sem_post(&mutex);

        // Signal that there's an empty slot
        sem_post(&empty);

        // If the buffer becomes empty, show that the consumer is waiting
        if (count == 0) {
            printf("Consumer: Buffer Empty\n");
        }

        sleep(2);  // Simulate work
    }
    return NULL;
}

int main() {
    pthread_t producer_thread, consumer_thread;

    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE);  // Initially all slots are empty
    sem_init(&full, 0, 0);             // No slots are full initially
    sem_init(&mutex, 0, 1);            // Mutex initialized to 1 (binary semaphore)

    // Create producer and consumer threads
    pthread_create(&producer_thread, NULL, insertbuffer, NULL);
    pthread_create(&consumer_thread, NULL, readbuffer, NULL);

    // Wait for both threads to finish
    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);

    // Destroy the semaphores
    sem_destroy(&empty);
    sem_destroy(&full);
    sem_destroy(&mutex);

    printf("All threads completed. Program finished.\n");
    return 0;
}
