# 12  20 / 2024

### Processes in one application needs to be coordinated / synchronized to be able to work together. 
### The processes have to agree on the method of communication.

#### Agreements
- Middleware must be good enough to handle the failure of some components of the application.

![alt text](image.png)

## Distributed locks (Distributed Mutual Exclusion)
- In operating system we have mutex like :
  - Semmaphore
    - x as lock
      - r(read) x
      - x + 1
      - w(write) x
    - These 3 operations are indivisible
    - If not all are executed, might have interrupt
- In Distributed Mutual Exclusion, we can't use indivisible operations
- Solved by hw indivisible operation "spin-lock" instruction

## Consensus
- We assume processes are not perfect
- So we need an agreement to handle those

![alt text](image-1.png)
> CS is critical section(of code), usually involve shared resource.(go in and out the door at the same time. Intefering 
### Application level protocol makes sure only one is entering the shared resource at the same time

### Requirements
- Safety, makes sure only one is entering the shared resource at the same time

![alt text](image-2.png)
## Central Server Algorithm
- Requests token from Server, that will be used to access the shared resources
- The diagram is not good enough, the happen-before ordering is not garunteed

![alt text](image-3.png)
- Example Consensus : Everyone hears the request and decide what they want to do.
- ![alt text](image-4.png)
- Not recieving ok from everyone(ignoring means no / using the resource), will queue the request and not replying.
- The clock does not need to be accurate, when using a timestamp.
  - But in this multitask solution, if the local clock of each client are not the same, this won't work.
  - Time at P1 = 200
  - Time at P2 = 150
  - Time at P3 = 6000
  - P1 and P3 request for CS access, P3 will never get it because it is 5800 slower than P1 and when checking timestamp.
  - With monotonically increasing clock.

![alt text](image-5.png)
- if you send the request to each of the reciepients one by one and your program crashes, only some of the process will get it.

![alt text](image-6.png)

![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)
- Multicast must go to all the processesin thegroup, including the requesting process. It's deliver all or deliver nothing.
- trick is to be ready before delivering. Ask every process first if they are ready. 

![alt text](image-10.png)
- When getting a multicast, each process also multicasts.
- Redundant, but sure.
![alt text](image-11.png)
- P sent to some processes and crashes. Q relay the messages to other processes, eventhough P already fails

![alt text](image-12.png)

![alt text](image-13.png)
# **There are 4 pages of this diagram. Very important, check out in tablet**

![alt text](image-14.png)

![alt text](image-15.png)

![alt text](image-16.png)

![alt text](image-17.png)
# Ask like this in midterm :
- If move 25 to below 27, what happens?
  - Lose total ordering but still have FIFO and Causal ordering
- If move 24 to below 27, what happens?
  - Lost Total and causal ordering

> Total ordering is very useful, simple but expensive

