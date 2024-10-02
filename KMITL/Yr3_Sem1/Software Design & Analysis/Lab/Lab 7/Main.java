import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;


class ChocolateBar {
    private final String type;
    private final int uniqueId;

    public ChocolateBar(String type, int uniqueId) {
        this.type = type;
        this.uniqueId = uniqueId;
    }

    public String getType() {
        return type;
    }

    public int getUniqueId() {
        return uniqueId;
    }

    @Override
    public String toString() {
        return "ChocolateBar{" +
                "type='" + type + '\'' +
                ", uniqueId=" + uniqueId +
                '}';
    }
}


class ChocolateFactory {
    private static volatile ChocolateFactory instance;
    private final Map<String, Integer> idCounters;

    private ChocolateFactory() {
        idCounters = new HashMap<>();
    }

    public static ChocolateFactory getInstance() {
        if (instance == null) {
            synchronized (ChocolateFactory.class) {
                if (instance == null) {
                    instance = new ChocolateFactory();
                }
            }
        }
        return instance;
    }

    public synchronized ChocolateBar createChocolateBar(String type) {
        idCounters.putIfAbsent(type, 0);
        int uniqueId = idCounters.computeIfPresent(type, (k, v) -> v + 1);
        return new ChocolateBar(type, uniqueId);
    }
}


public class Main {
    public static void main(String[] args) {
        // Runnable task to produce chocolate bars
        Runnable WonkaProductionTask = () -> {
            ChocolateFactory factory = ChocolateFactory.getInstance();
            for (int i = 0; i < 5; i++) {
                ChocolateBar bar = factory.createChocolateBar("Wonka Bar");
                System.out.println(Thread.currentThread().getName() + " produced " + bar);
            }
        };

        Runnable OompaloompaProductionTask = () -> {
            ChocolateFactory factory = ChocolateFactory.getInstance();
            for (int i = 0; i < 5; i++) {
                ChocolateBar bar = factory.createChocolateBar("Oompaloompa Bar");
                System.out.println(Thread.currentThread().getName() + " produced " + bar);
            }
        };

        Thread thread1 = new Thread(WonkaProductionTask);
        Thread thread2 = new Thread(WonkaProductionTask);
        Thread thread3 = new Thread(OompaloompaProductionTask);
        Thread thread4 = new Thread(OompaloompaProductionTask);


        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();
        try {
            thread1.join();
            thread2.join();
            thread3.join();
            thread4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
