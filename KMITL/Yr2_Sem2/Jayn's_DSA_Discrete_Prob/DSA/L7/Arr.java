public class ArrayDeque<T> {
    private T[] items;
    private int size;
    private int front;
    private int rear;

    private static final int INITIAL_CAPACITY = 8;
    private static final double MIN_USAGE_FACTOR = 0.25;

    public ArrayDeque() {
        items = (T[]) new Object[INITIAL_CAPACITY];
        size = 0;
        front = 0;
        rear = 0;
    }

    public ArrayDeque(ArrayDeque<T> other) {
        items = (T[]) new Object[other.items.length];
        size = other.size;
        front = 0;
        rear = size - 1;
        System.arraycopy(other.items, 0, items, 0, other.items.length);
    }

    // private void resize(int capacity) {
    //     T[] newArray = (T[]) new Object[capacity];
    //     for (int i = 0; i < size; i++) {
    //         newArray[i] = items[(front + i) % items.length];
    //     }
    //     items = newArray;
    //     front = 0;
    //     rear = size - 1;
    // }

    // public void addFirst(T item) {
    //     if (size == items.length) {
    //         resize(items.length * 2);
    //     }
    //     front = (front - 1 + items.length) % items.length;
    //     items[front] = item;
    //     size++;
    // }

    // public void addLast(T item) {
    //     if (size == items.length) {
    //         resize(items.length * 2);
    //     }
    //     rear = (rear + 1) % items.length;
    //     items[rear] = item;
    //     size++;
    // }

    // public T removeFirst() {
    //     if (isEmpty()) {
    //         return null;
    //     }
    //     T removedItem = items[front];
    //     front = (front + 1) % items.length;
    //     size--;

    //     if (size > 0 && size < items.length * MIN_USAGE_FACTOR) {
    //         resize(items.length / 2);
    //     }

    //     return removedItem;
    // }

    // public T removeLast() {
    //     if (isEmpty()) {
    //         return null;
    //     }
    //     T removedItem = items[rear];
    //     rear = (rear - 1 + items.length) % items.length;
    //     size--;

    //     if (size > 0 && size < items.length * MIN_USAGE_FACTOR) {
    //         resize(items.length / 2);
    //     }

    //     return removedItem;
    // }

    // public T get(int index) {
    //     if (index < 0 || index >= size) {
    //         return null;
    //     }
    //     return items[(front + index) % items.length];
    // }

    // public int size() {
    //     return size;
    // }

    // public boolean isEmpty() {
    //     return size == 0;
    // }

    public void printDeque() {
        for (int i = 0; i < size; i++) {
            System.out.print(items[(front + i) % items.length] + " ");
        }
        System.out.println();
    }
}
