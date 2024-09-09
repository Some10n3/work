#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void display_menu() {
    printf("Menu:\n");
    printf("1. ls\n");
    printf("2. date\n");
    printf("3. ps\n");
    printf("0. exit\n");
    printf("Enter your choice: ");
}

int main() {
    int choice;
    pid_t pid;

    while (1) {
        display_menu();
        scanf("%d", &choice);

        if (choice == 0) {
            printf("Exiting...\n");
            break;
        }

        pid = fork();
        if (pid < 0) {
            perror("fork failed");
            exit(1);
        } else if (pid == 0) { // Child process
            switch (choice) {
                case 1:
                    execlp("ls", "ls", NULL);
                    break;
                case 2:
                    execlp("date", "date", NULL);
                    break;
                case 3:
                    execlp("ps", "ps", NULL);
                    break;
                default:
                    printf("Invalid choice!\n");
                    exit(1);
            }
            perror("execlp failed"); // This line will be reached only if execlp fails
            exit(1);
        } else { // Parent process
            wait(NULL); // Wait for child process to finish
        }
    }

    return 0;
}
