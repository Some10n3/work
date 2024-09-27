public class BoundedBuffer {
    private static final int BUFFER_SIZE = 5;  
    private int count;  
    private int in;     
    private int out;    
    private Object[] buffer;  

    
    public BoundedBuffer() {
        count = 0;   
        in = 0;      
        out = 0;     
        buffer = new Object[BUFFER_SIZE];  
    }

    
    public synchronized void insert(Object item) {
        while (count == BUFFER_SIZE) {
            try {
                System.out.println("Producer: Buffer Full");
                wait();  
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); 
            }
        }

        
        buffer[in] = item;
        in = (in + 1) % BUFFER_SIZE;  
        count++;

        System.out.println("Producer inserted: " + item + " Buffer size = " + count);

        notifyAll();  
    }

    
    public synchronized Object remove() {
        while (count == 0) {
            try {
                System.out.println("Consumer: Buffer Empty");
                wait();  
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); 
            }
        }

        
        Object item = buffer[out];
        out = (out + 1) % BUFFER_SIZE;  
        count--;

        System.out.println("Consumer consumed: " + item + " Buffer size = " + count);

        notifyAll();  

        return item;
    }

    public static void main(String[] args) {
        BoundedBuffer buffer = new BoundedBuffer();  

        Producer producer = new Producer(buffer);  
        Consumer consumer = new Consumer(buffer);  

        producer.start();  
        consumer.start();  

        
        try {
            producer.join();
            consumer.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("All threads completed. Program finished.");
    }
}


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
                sleep(1000);  
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();  
            }
        }
    }
}


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
                sleep(1500);  
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();  
            }
        }
    }
}
