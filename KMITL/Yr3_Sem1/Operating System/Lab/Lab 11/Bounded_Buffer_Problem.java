import java.util.concurrent.Semaphore;

class BoundedBuffer {
    private final int[] buffer;
    private int count, in, out;

    // Semaphores for controlling buffer access
    private final Semaphore mutex = new Semaphore(1); // Controls access to the critical section
    private final Semaphore empty;  // Counts empty slots in the buffer
    private final Semaphore full;   // Counts full slots in the buffer

    public BoundedBuffer(int size) {
        buffer = new int[size];
        count = in = out = 0;
        empty = new Semaphore(size);  // Initially, the buffer has 'size' empty slots
        full = new Semaphore(0);      // Initially, the buffer has 0 full slots
    }

    public void produce(int item) throws InterruptedException {
        empty.acquire();  // wait(empty): Wait for an empty slot
        mutex.acquire();  // wait(mutex): Wait for exclusive access to buffer

        // Critical section: Add the item to the buffer
        buffer[in] = item;
        in = (in + 1) % buffer.length;
        count++;
        System.out.println("Producer Entered " + item + " Buffer Size = " + count);

        mutex.release();  // signal(mutex): Release access to buffer
        full.release();   // signal(full): Signal that there is a full slot
    }

    public void consume() throws InterruptedException {
        full.acquire();   // wait(full): Wait for a full slot
        mutex.acquire();  // wait(mutex): Wait for exclusive access to buffer

        // Critical section: Remove an item from the buffer
        int item = buffer[out];
        out = (out + 1) % buffer.length;
        count--;
        System.out.println("Consumer Consumed " + item + " Buffer " + (count == 0 ? "EMPTY" : "Size = " + count));

        mutex.release();  // signal(mutex): Release access to buffer
        empty.release();  // signal(empty): Signal that there is an empty slot
    }
}

class Producer implements Runnable {
    private final BoundedBuffer buffer;

    public Producer(BoundedBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 20; i++) {
                buffer.produce(i);
                Thread.sleep(100);  // Simulate the time taken to produce an item
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

class Consumer implements Runnable {
    private final BoundedBuffer buffer;

    public Consumer(BoundedBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 20; i++) {
                buffer.consume();
                Thread.sleep(150);  // Simulate the time taken to consume an item
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

public class Bounded_Buffer_Problem {
    public static void main(String[] args) {
        BoundedBuffer buffer = new BoundedBuffer(5);  // Set buffer size to 5

        Producer producer = new Producer(buffer);
        Consumer consumer = new Consumer(buffer);

        // Create and start producer and consumer threads
        Thread producerThread = new Thread(producer);
        Thread consumerThread = new Thread(consumer);

        producerThread.start();
        consumerThread.start();
    }
}
