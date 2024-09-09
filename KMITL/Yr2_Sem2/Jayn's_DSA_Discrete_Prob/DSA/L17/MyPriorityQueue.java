import java.util.Arrays;
import java.util.Comparator;
import java.util.NoSuchElementException;

public class MyPriorityQueue<T> {

    //implement binary heap
    private T[] heap;
    private int size;
    private Comparator<T> cc;

    public MyPriorityQueue(Comparator<T> cc) {
        this(cc, 10);
    }

    public MyPriorityQueue(Comparator<T> cc, int capacity) {
        this.cc = cc;
        heap = (T[]) new Object[capacity];
        size = 0;
    }

    public int left(int i) {
        return 2 * i + 1;
    }

    public int right(int i) {
        return 2 * i + 2;
    }

    public int parent(int i) {
        return (i - 1) / 2;
    }

    public void enqueue(T value) {
        if (size == heap.length) {
            heap = Arrays.copyOf(heap, size * 2);
        }
        heap[size] = value;
        swim(size);
        size++;
    }

    public void dequeue() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        heap[0] = heap[size - 1];
        size--;
        sink(0);
    }

    public void swim(int k) {
        while (k > 0 && cc.compare(heap[parent(k)], heap[k]) < 0) {
            swap(k, parent(k));
            k = parent(k);
        }
    }

    public void sink(int k) {
        while (left(k) < size) {
            int j = left(k);
            if (right(k) < size && cc.compare(heap[right(k)], heap[left(k)]) > 0) {
                j = right(k);
            }
            if (cc.compare(heap[k], heap[j]) > 0) {
                break;
            }
            swap(k, j);
            k = j;
        }
    }

    public void swap(int i, int j) {
        T temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    public T remove() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        T result = heap[0];
        heap[0] = heap[size - 1];
        size--;
        sink(0);
        return result;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public T findMax() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        return heap[0];
    }

    public int size() {
        return size;
    }

    public void removeMax() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        swap(0, size - 1);
        size--;
        sink(0);
    }

    public String toString() {
        return Arrays.toString(Arrays.copyOf(heap, size));
    }

    public static void main(String[] args) {
        MyPriorityQueue<Integer> pq = new MyPriorityQueue<>(Integer::compareTo);
        pq.enqueue(3);
        pq.enqueue(2);
        pq.enqueue(15);
        pq.enqueue(5);
        pq.enqueue(4);
        pq.enqueue(45);
        System.out.println(pq.findMax());
        System.out.println(pq);
        System.out.println(pq.isEmpty());
        pq.removeMax();
        System.out.println(pq);
        // System.out.println(pq.remove());
        // System.out.println(pq.remove());
        // System.out.println(pq);
    }
}
