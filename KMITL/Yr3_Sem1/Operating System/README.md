<style>
img {
  width: 400px;
}
</style>

# Message Passing

![](./pics(slide5)/Interprocess_Communication.png)
IPC facility provides two operations :
- send(message)
- recieve(message)

***Messages can be passed in one direction or bidirectional**

## Synchronization
- Message passing can be blocking (synchronous), or non blocking(asynchronous)

### Blocking
- blocking send
    - Sender block until the reciever said it recieves the message
- blocking recieve
    - when reciever goes to read message, if the message not arrived it waits til the message arrives(waiting for ACK)

### Non Blocking
- Sender might not care if the reciever recieve the messages or not
- non blocking send
    - sender send message and continue
- non blocking recieve
    - reciever recieve a valid message or null

## Pipes
- One way communication
- State which one is sender and which one is reciever
- takes an array of two integers. It fills in the array with two file descriptors that can be used for low-level I/O.

![](./pics(slide5)/Creating_Pipe.png)
![](./pics(slide5)/Read_Write.png)


![](./pics(slide5)/Fork_and_Pipe.png)
- Parent has to create the pipe first, before forking
- So the child can get the pipe too


![](./pics(slide5)/Fork_and_Pipe2.png)
- Both Parent and Child has write and read ends
- Sender closes read end while reciever close the write end
``` C
pipe.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#define SIZE 1024
#define READ_SIZE 5
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
    close(pfd[1]);
    while ((nread = read(pfd[0], buf_read, READ_SIZE)) != 0) {
      printf("child read %s\n", buf_read);
    }
    close(pfd[0]);
  } else {
    /* parent */
      close(pfd[0]);
      strcpy(buf, "hello world, hello mars, hello universe");
      //sleep(2);
      /* include null terminator in write */
      write(pfd[1], buf, strlen(buf)+1);
      //write(pfd[1], buf, strlen(buf));
      close(pfd[1]);
      wait(NULL);
  }
  exit(0);
}
```

![](./pics(slide5)/No_backslash.png)
![](./pics(slide5)/No_backslash2.png)
- If you don't +1 for the back slash, it will take the last char of the previous line

## fd 0 1 and 2 are reserved by os 
- ***fd is file descriptor**
- 0 -> stdin
- 1 -> stdout
- 2 -> stderr

![](./pics(slide5)/Pipe_Example.png)
- | is pipe
- in "ls | wc", the pipe redirects the output of ls to wc then wc will count them
- pass data with stdin (fd1) to stdout (fd2) through pipe with fd3 and fd4
- ***fd1 is stdout, fd0 is stdin**

![](./pics(slide5)/wc.png)
- 39 lines / number of files
- 66 words / 
- 568 characters

![](./pics(slide5)/Filename_with_Space.png)
- 5 lines (5 files)
- 6 words
- 37 characters
- use -l (lines) instead of -w (words), because words may read one file as two if the file name contains a space

## dup2 function
![](./pics(slide5)/dup2.png)
- use dup2 to join fd1 to fd3 adn fd4 to fd0
- dup2 is dupto not duptwo

``` C
dup2.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
  int pfd[2];
  int pid;

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
  if (pid == 0) // child
  { 
    close(pfd[0]); // close read end
    dup2(pfd[1],1 ); // dupe write end
    close(pfd[1]); // close og write end
    execlp("ls", "ls",NULL); // exec ls
    perror("ls failed"); // error if exec fails
    exit(3);
  } else {        // parent
    close(pfd[1]); // close write end
    dup2(pfd[0], 0); // dupe read end
    close(pfd[0]); // close og read end
    execlp("wc", "wc",NULL); // exec wc with data from child
    perror("wc failed");
    exit(4);
  }
  exit(0);
}
```

``` C
twopipe.c
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define SIZE 1024

int main(int argc, char **argv)
{
  int pfd1[2];
  int pfd2[2]; 
  int nread;
  int pid;
  int status;
  char buf[SIZE];

  if (pipe(pfd1) == -1) {
    perror("pipe failed");
    exit(1);
  }
  if (pipe(pfd2) == -1) {
	perror("pipe failed");
	exit(1);
  }
  if ((pid = fork()) < 0) {
    perror("fork failed");
    exit(2);
  }
  if (pid == 0) {
    /* child */
    close(pfd1[1]);
    close(pfd2[0]);
    while ((nread = read(pfd1[0], buf, SIZE)) != 0) {	
    	printf("child read %s\n", buf);
    }
    close(pfd1[0]);
    strcpy(buf, "I am fine thank you");
    write(pfd2[1], buf, strlen(buf) + 1);
    close(pfd2[1]);	
  } else {
    /* parent */
    close(pfd1[0]);
    close(pfd2[1]);
    strcpy(buf, "How are you");
    /* include null terminator in write */
    write(pfd1[1], buf,strlen(buf)+1);
    close(pfd1[1]);
    while ((nread = read(pfd2[0], buf, SIZE)) != 0) {
	    printf("Parent read %s\n", buf);	 
    }
    close(pfd2[0]);
  }
  exit(0);
}
```

# Shared memory
- Two processes share one memory
- Uses the shared memory to exchange data

- Process that creates a shared memory is called server
- Process that usese the shared memory is called client

- There's no protection on the access from other processes
- Can only forced them to only read / write (give them access to only some operation)

## Race condition
- processes race each other to update the daata
- prevent with synchronization

## shared mem functions
- shmget() 
    - return shm id
- shmat() 
    - shared mem attatch
    - use to links shared mem to existing storage space
- shmdt() 
    - shared mem detatch
    - use to detatch shared mem to existing storage space
- shmctl() shared mem control
    - remove shared memory

### flow of server and client
- ***Server should perform these tasks before the clients**
- calls shmget to get the shmid then attatch the client's/server's address to the shared mem with the key(shmid). 
- Do some task
- Detatch the shm from the space
- (only server do this) calls shmctl() to remove shared memory

## key
- (key is int redefined as key_t)
- a key is then generated with ftok()
- A unique key can be generated with IPC_Private() (garunteed to get a unique key)
- IPC can only be used in the same family of process, (parent, child). Other processes can't access them
- If not parent / chile, has to use ftok()

![](./pics(slide5)/key.png)

## ftok()
![](./pics(slide5)/ftok.png)
![](./pics(slide5)/ftok2.png)
- . is the path to the current directory
- some other process can get this key with the path to this directory

## Permissions
![](./pics(slide5)/perm.png)
- permission can be separated into 3 groups
- - --- --- --- separate into (the first one just sayys if it's directory or not)
    - perm for owner
    - perm for user in the same grouup as the owner
    - perm for other users
- "---"
    - perm for read, write and execute
![](./pics(slide5)/perm2.png)
- can be represented as an octadecimal

## shmget()
![](./pics(slide5)/shmget.png)
- (0666) means allow r/w to all processes that can access this shm
    - 0666 is from the permission of the file
    - rw- rw- rw-
    -  6   6   6 
    - 0666 means everyone on the system can read and write to this file
![](./pics(slide5)/chmod)
- change mode to 666 with chmod






![](./pics(slide5)/)