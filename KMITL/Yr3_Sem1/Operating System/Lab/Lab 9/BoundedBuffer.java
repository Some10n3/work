public class BoundedBuffer {
    private static final int BUFFER_SIZE = 5;  // Bounded buffer size
    private int count;  // Number of items in the buffer
    private int in;     // Index for the producer to insert items
    private int out;    // Index for the consumer to remove items
    private Object[] buffer;  // Shared buffer

    // Constructor to initialize buffer and related variables
    public BoundedBuffer() {
        count = 0;   //A: Initially, buffer is empty
        in = 0;      //B: Insert position starts at 0
        out = 0;     //C: Remove position starts at 0
        buffer = new Object[BUFFER_SIZE];  // Initialize the buffer
    }

    // Producer calls this method to insert an item into the buffer
    public synchronized void insert(Object item) {
        while (count == BUFFER_SIZE) {
            try {
                System.out.println("Producer: Buffer Full");
                wait();  // Wait if the buffer is full
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); // Preserve the interrupt status
            }
        }

        // Insert the item into the buffer
        buffer[in] = item;
        in = (in + 1) % BUFFER_SIZE;  // Circular buffer logic
        count++;

        System.out.println("Producer inserted: " + item + " Buffer size = " + count);

        notifyAll();  // Notify consumer that an item is available
    }

    // Consumer calls this method to remove an item from the buffer
    public synchronized Object remove() {
        while (count == 0) {
            try {
                System.out.println("Consumer: Buffer Empty");
                wait();  // Wait if the buffer is empty
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); // Preserve the interrupt status
            }
        }

        // Remove the item from the buffer
        Object item = buffer[out];
        out = (out + 1) % BUFFER_SIZE;  // Circular buffer logic
        count--;

        System.out.println("Consumer consumed: " + item + " Buffer size = " + count);

        notifyAll();  // Notify producer that space is available

        return item;
    }

    public static void main(String[] args) {
        BoundedBuffer buffer = new BoundedBuffer();  // Shared buffer

        Producer producer = new Producer(buffer);  // Create producer thread
        Consumer consumer = new Consumer(buffer);  // Create consumer thread

        producer.start();  // Start producer thread
        consumer.start();  // Start consumer thread

        // Wait for both threads to complete
        try {
            producer.join();
            consumer.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("All threads completed. Program finished.");
    }
}

// Producer class that inserts items into the buffer
class Producer extends Thread {
    private BoundedBuffer buffer;

    public Producer(BoundedBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        for (int i = 0; i < 41; i++) {  
            buffer.insert(i);
            try {
                sleep(1000);  // Simulate time taken to produce an item
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();  // Preserve the interrupt status
            }
        }
    }
}

// Consumer class that removes items from the buffer
class Consumer extends Thread {
    private BoundedBuffer buffer;

    public Consumer(BoundedBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        for (int i = 0; i < 41; i++) {  
            buffer.remove();
            try {
                sleep(1500);  // Simulate time taken to consume an item
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();  // Preserve the interrupt status
            }
        }
    }
}
