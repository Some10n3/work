#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/shm.h>
#include <sys/ipc.h>

int main(int argc, char **argv) {
    int shmid;
    int *shm_ptr;
    pid_t pid;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <num>\n", argv[0]);
        exit(1);
    }

    int num = atoi(argv[1]);

    // Create shared memory with IPC_PRIVATE
    shmid = shmget(IPC_PRIVATE, sizeof(int), IPC_CREAT | 0666);
    if (shmid < 0) {
        perror("shmget failed");
        exit(2);
    }
    printf("Parent: I have created a shared memory for result...\n");

    // Attach shared memory
    shm_ptr = (int *)shmat(shmid, NULL, 0);
    if (shm_ptr == (int *)-1) {
        perror("shmat failed");
        exit(3);
    }
    printf("Parent: I have attached the shared memory...\n");

    // Fork process
    printf("Parent: I am about to fork a child process...\n");
    if ((pid = fork()) < 0) {
        perror("fork failed");
        exit(4);
    }

    if (pid == 0) {  // Child process (client)
        printf("Child: I am calculating\n");
        int result = 0;

        for (int i = 1; i <= num; i++) {
            result += i;
        }

        *shm_ptr = result;  // Write result to shared memory
        printf("Child: The result is %d\n", result);

        // Detach shared memory (child)
        if (shmdt(shm_ptr) == -1) {
            perror("Child: shmdt failed");
            exit(5);
        }
        printf("Child: I have detached the shared memory...\n");

        printf("Child: Goodbye\n");
        exit(0);
    } else {  // Parent process (server)
        printf("Parent: Waiting for my child\n");
        wait(NULL);

        // Read the result from shared memory
        printf("Parent: sum from my child is %d\n", *shm_ptr);

        // Detach shared memory (parent)
        if (shmdt(shm_ptr) == -1) {
            perror("Parent: shmdt failed");
            exit(6);
        }
        printf("Parent: I have detached the shared memory...\n");

        // Remove shared memory (server only)
        if (shmctl(shmid, IPC_RMID, NULL) == -1) {
            perror("shmctl failed");
            exit(7);
        }
        printf("Parent: I have removed the shared memory...\n");
        printf("Parent: Goodbye\n");
    }

    return 0;
}
