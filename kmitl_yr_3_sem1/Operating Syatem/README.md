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