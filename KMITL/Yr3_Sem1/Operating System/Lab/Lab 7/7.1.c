#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#define SIZE 1024
#define READ_SIZE 500
int main(int argc, char **argv)
{
  int pfd[2];
  int nread;
  int pid;
  char buf[SIZE];
  char buf_read[READ_SIZE+1];
  if (pipe(pfd) == -1)
  {
    perror("pipe failed");
    exit(1);
  }
  if ((pid = fork()) < 0)
  {
    perror("fork failed");
    exit(2);
  }
  if (pid == 0)
  {
    /* child */
    printf("child: calculating sum of 1 to %s\n", argv[1]);
    close(pfd[0]);
    int result = 0;
    int arg = atoi(argv[1]);
    for (int i = 1; i <= arg; i++)
    {
      result += i;
    }
    printf("child: The result is %d\n", result);
    sprintf(buf, "%d", result);
    //sleep(2);
    printf("child: sending data\n");
    write(pfd[1], buf, strlen(buf)+1);
    close(pfd[1]);
    printf("child: goodbye\n");

  } else {
    /* parent */
    printf("parent: waiting for child\n");
    wait(NULL);
    close(pfd[1]);
    while ((nread = read(pfd[0], buf_read, READ_SIZE)) != 0) {
    printf("parent: sum from my child is %s\n", buf_read);
    }
    close(pfd[0]);
    printf("parent: goodbye\n");
  }

  exit(0);
}