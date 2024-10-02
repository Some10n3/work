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
- shmad() 
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
    
![](./pics(slide5)/chmod.png)
- change mode to 666 with chmod

![](./pics(slide5)/Ex_shmget.png)
- use IPC_PRIVATE
- 4 bytes of mem (integer sized) as shared mem
- mode 0666

## shmat()
![](./pics(slide5)/shmat.png)
- use the shm address created by system (send null ptr, like in adlx)
- use the flags when it is created (send null ptr, like in adlx)
- can use other flags / addr but in this class we only use this, like using macro SHM_RDONLY predefined by system.


``` C
shm_parent_child.c

#include  <stdio.h>
#include  <stdlib.h>
#include  <sys/types.h>
#include  <sys/ipc.h>
#include  <sys/shm.h>
#include <sys/wait.h>
#include <unistd.h>

void  ClientProcess(int []);

void  main(int  argc, char *argv[])
{
     int    shm_id;
     int    *shm_ptr;
     pid_t  pid;
     int    status;
     
     if (argc != 5) {
          printf("Use: %s #1 #2 #3 #4\n", argv[0]);
          exit(1);
     }
     
     shm_id = shmget(IPC_PRIVATE, 4*sizeof(int), IPC_CREAT | 0666);
     if (shm_id < 0) {
          printf("*** shmget error (server) ***\n");
          exit(1);
     }
     printf("Server has received a shared memory of four integers...\n");
     
     shm_ptr = (int *) shmat(shm_id, NULL, 0);
     if ( shm_ptr == NULL) {
          printf("*** shmat error (server) ***\n");
          exit(1);
     }
     printf("Server has attached the shared memory...\n");
     
     shm_ptr[0] = atoi(argv[1]);
     shm_ptr[1] = atoi(argv[2]);
     shm_ptr[2] = atoi(argv[3]);
     shm_ptr[3] = atoi(argv[4]);
     printf("Server has filled %d %d %d %d in shared memory...\n",
            shm_ptr[0], shm_ptr[1], shm_ptr[2], shm_ptr[3]);
            
     printf("Server is about to fork a child process...\n");
     pid = fork();
     if (pid < 0) {
          printf("*** fork error (server) ***\n");
          exit(1);
     }
     else if (pid == 0) {
          ClientProcess(shm_ptr);
          exit(0);
     }
          
     wait(&status);
     printf("Server has detected the completion of its child...\n");
     shmdt((void *) shm_ptr);
     printf("Server has detached its shared memory...\n");
     shmctl(shm_id, IPC_RMID, NULL);
     printf("Server has removed its shared memory...\n");
     printf("Server exits...\n");
     exit(0);
}

void  ClientProcess(int  share_mem[])
{
     printf("   Client process started\n");
     printf("   Client found %d %d %d %d in shared memory\n",
                share_mem[0], share_mem[1], share_mem[2], share_mem[3]);
     printf("   Client is about to exit\n");
}
```

<!-- ![](./pics(slide5)/ -->

# Process synchronization
- To prevent Consumer to get the outdated / duplicated data
- Prevent race condition, but may lead to deadlock

## Producer
![](./pics(slide6)/producer.png)
- Write data from first slot, until the last slot. After that start at first slot again
- write data forever
- count data added to buffer
- prevent lost data of the consumer

## Consumer
![](./pics(slide6)/consumer.png)
- Check count with buffer size before reading to prevent reading duplicated data

## Race Condition
- Condition that more than one process update data at the same time. Result might be incorrect based on the last process that edit the data
- so the incrementation and decrementation don't get fucked when updating with multiple processes at the same time
![](./pics(slide6)/race_cond.png)
- Incorrect result, register 2 read the unchanged value of register 1


# watch later

## Bakery Algorithm

- Some problem
- Solved with Semaphore

## Semaphore
- one binary two counting
- OS provide Semaphore for us. We apply it ourself

## Reader-Writer Problem
- Related to DB
- DB might allow one process to allow writing data at a time
- Might have reader while writing, bad
- If the writer is writing, readers can't read

### Writer process structure
![alt text](./pics(slide6)/writer.png)
- Check if there's reader. If not, write

### Reader process structure
![alt text](./pics(slide6)/reader.png)


# Exam might ask how u use semaphore to solve these
- no framework, guideline
- You have to think of how to use the semaphore urself

## Diner philosopher problem
![alt text](./pics(slide6)/diner_philosopher.png)
- 5 chopsticks, 5 people
- To eat, need a pair (2chopsticks)
- when philisopher want to eat, pick left and right chopsticks to make pair
- If the left chopstick is being used by another philosopher, the current philosopher has to wait
- Use semaphore to solve this
- We don't have enough resource for the process
- ***Use semaphore to prevent 2 philosophers to hold same chopstick at the same time**

![alt text](./pics(slide6)/diner_philosopher_code.png)
- wait(chopstick[i]) : wait left chopstick
- wait(chopstick[(i + 1) % 5]) : wait right chopstick
- signal(chopstick[i]) : take left chopstick and eat
- signal(chopstick[(i + 1) % 5]) : take right chopstick and eat
- Get deadlock because if everyone picks left chopsticks, they will wait for right chopstick from eachother

![alt text](./pics(slide6)/bad_semaphore.png)
- Signal before wait, adding extra marble to the jar


![alt text](image.png)
![alt text](image-1.png)
- sem_init(&mutex, 0, 1)
  - 0 means this mutex will only be used by the threads created by this process only (shared among threads by this process)
- Linux and mac have to use named semaphore
![alt text](image-2.png)
- sem_init to sem_open
- sem_destroy to sem_close and sem_unlink

![alt text](image-3.png)
- binary semaphore (mutex lock)

![alt text](image-4.png)
- semaphore is not used to allocate resource
- Just to ensure that no philosopher has the same chopstick(resource)

## Monitor
![alt text](image-5.png)
- OOP
- Use struct for combining data in a single unit
- Only one process active in the monitor means garunteed mutual exclusive
- easier to use then semaphore
- flexibility
- ***No deadlock**

![alt text](image-6.png)
![alt text](image-7.png)

![alt text](./pics(slide6)/soln2dining.png)
![alt text](./pics(slide6)/soln2dining2.png)
- Fixed deadlock
- But new problem
- Starvation
  - Some process may wait forever

# Java synchronization
![alt text](image-8.png)
![alt text](image-9.png)

## Synchronized method
- When a thread calls a synchronized, the thread will be the owner of the lock (A lock will occur automatically, and released when the sync method is done executing)
- other thread can't call the synchronized method within this object while one is calling

![alt text](image-10.png)
- The entry set is the same as the entry queue of the monitor in C
- Use wait and notify instead of wait and signal

![alt text](image-11.png)
- when lock owner calls wait, the object will be unlocked and continue to wait queue

### Notify method
![alt text](image-12.png)
- Wake up thread in wait set and it will go back to entry queue 
- Can't choose which thread to be waken up from the wait set (**Bounded waiting**)
- Depends on JVM

![alt text](image-13.png)
- by producer to send data

![alt text](image-14.png)
- by consumer to read data

### yield() is not the same as wait()
- yield() : I'm not working and allow other thread to work
- you might think that using yield() instead of wait()
- but yeild doesn't release the lock
- consumer won't be able to call the object anyway, object is still locked
- wait release the lock and let other process continue

![alt text](image-15.png)
- acquire is wait
- release is signal
- (this is just the implementation, java now has built-in sephamore)
***Java < 5 doesn't provide semaphore**

![alt text](image-16.png)
- one sync method can be called at a time

![alt text](image-17.png)
- Java allows only synching a block and not the whole method
