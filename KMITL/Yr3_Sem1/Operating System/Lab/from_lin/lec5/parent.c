#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    if (argc != 5) {
        fprintf(stderr, "Usage: %s <num1> <num2> <num3> <num4>\n", argv[0]);
        return 1;
    }

    pid_t pid1, pid2;
    int status1, status2;

    
    pid1 = fork();
    if (pid1 < 0) {
        perror("fork failed");
        exit(1);
    } else if (pid1 == 0) { 
        execl("./child", "./child", argv[1], argv[2], NULL);
        perror("execl failed");
        exit(1);
    }

    
    pid2 = fork();
    if (pid2 < 0) {
        perror("fork failed");
        exit(1);
    } else if (pid2 == 0) { 
        execl("./child", "./child", argv[3], argv[4], NULL);
        perror("execl failed");
        exit(1);
    }

    
    waitpid(pid1, &status1, 0);
    if (WIFEXITED(status1)) {
        status1 = WEXITSTATUS(status1);
    } else {
        fprintf(stderr, "First child did not exit normally\n");
        status1 = 0;
    }

    
    waitpid(pid2, &status2, 0);
    if (WIFEXITED(status2)) {
        status2 = WEXITSTATUS(status2);
    } else {
        fprintf(stderr, "Second child did not exit normally\n");
        status2 = 0;
    }

    
    int final_result = status1 + status2;
    printf("The final result is: %d\n", final_result);

    return 0;
}
