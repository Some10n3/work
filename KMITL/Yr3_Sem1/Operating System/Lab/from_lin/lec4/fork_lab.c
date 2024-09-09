#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;

    printf("I am parent\n");

    for (int i = 0; i < 5; i++) {
        pid = fork();

        if (pid == 0) {  // Child process
            printf("I am child %d\n", i);

            if (i % 2 == 0) {  // Even numbered children
                for (int j = 0; j < 4; j++) {
                    pid = fork();
                    if (pid == 0) {  // Sub-child process
                        printf("I am sub-child %d of the child %d\n", j, i);
                        return 0;
                    }
                }
            } else {  // Odd numbered children
                for (int j = 0; j < 5; j++) {
                    pid = fork();
                    if (pid == 0) {  // Sub-child process
                        printf("I am sub-child %d of the child %d\n", j, i);
                        return 0;
                    }
                }
            }

            // Wait for all sub-children to finish
            while (wait(NULL) > 0);
            return 0;
        }
    }

    // Parent waits for all children to finish
    while (wait(NULL) > 0);

    return 0;
}
