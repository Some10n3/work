import java.util.Arrays;

public class ArrayDeque<T> {
    private Object[] items;
    private int size;
    private int first;
    private int last;

    public ArrayDeque() {
        items = new Object[8];
        size = 0;
        first = 0;
        last = -1;
    }

    //here
    public ArrayDeque(ArrayDeque<T> other) {
        items = (T[]) new Object[other.items.length];
        size = other.size;
        first = 0;
        last = size - 1;
        System.arraycopy(other.items, 0, items, 0, other.items.length);
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void addFirst(T element) {
        ensureCapacity();
        System.out.println("first : " + first);
        System.out.println("items.length : " + items.length);
        System.out.println("(first - 1 + items.length) % items.length : " + (first - 1 + items.length) % items.length);
        System.out.println("items[(first - 1 + items.length) % items.length] : " + items[(first - 1 + items.length) % items.length]);
        System.out.println("");
            first = (first - 1 + items.length) % items.length;
        System.out.println("first : " + first);
        System.out.println("items.length : " + items.length);
        System.out.println("first : " + first);
            items[first] = element;
        System.out.println("items[first] : " + items[first]);
        System.out.println("");
            size++;
        System.out.println("");System.out.println("");
    }

    public void addLast(T element) {
        ensureCapacity();
        System.out.println("last : " + last);
        System.out.println("items.length : " + items.length);
        System.out.println("(last + 1) % items.length : " + (last + 1) % items.length);
        System.out.println("items[(last + 1) % items.length] : " + items[(last + 1) % items.length]);
        System.out.println("");
            last = (last + 1) % items.length;
        System.out.println("last : " + last);
        System.out.println("items.length : " + items.length);
        System.out.println("last : " + last);
            items[last] = element;
        System.out.println("items[last] : " + items[last]);
        System.out.println("");
            size++;
        System.out.println("");System.out.println("");
    }

    public T removeFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        T removed = (T) items[first];
        items[first] = null;
        first = (first + 1) % items.length;
        size--;
        return removed;
    }

    public T removeLast() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        T removed = (T) items[last];
        items[last] = null;
        last = (last - 1 + items.length) % items.length;
        size--;
        return removed;
    }

    public T getFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        return (T) items[first];
    }

    public T getLast() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        return (T) items[last];
    }

    private void ensureCapacity() {

        System.out.println("size : " + size);
        System.out.println("items.length : " + items.length);
        System.out.println("size == items.length : " + (size == items.length));
        System.out.println("");
        if (size == items.length) {
            int minCapacity = Math.max(4 * size, 16); // Ensure the new capacity is at least 4 times the current size or 16, whichever is larger
            int newCapacity = Math.max(items.length * 2, minCapacity);
            items = Arrays.copyOf(items, newCapacity);
        }
    }
    

    public String toString(){
        String result = "[ ";
        for (int i = 0; i < size; i++){
            result += items[(first + i) % items.length] + " ";
            System.out.println("first : " + first);
            System.out.println("i : " + i);
            System.out.println("items.length : " + items.length);
            System.out.println("(first + i) % items.length : " + (first + i) % items.length);
            System.out.println("items[(first + i) % items.length] : " + items[(first + i) % items.length]);
            System.out.println("");
        }
        return result + "]";
    }

    public static void main(String[] args) {
        ArrayDeque<Integer> deque = new ArrayDeque<>();

        deque.addFirst(1);
        deque.addLast(2);
        deque.addFirst(3);
        deque.addLast(4);
        System.out.println("");System.out.println("");System.out.println("");
        System.out.println("");System.out.println("");System.out.println("");
        System.out.println("");System.out.println("");System.out.println("");

        System.out.println("Size: " + deque.size());
        System.out.println("First element: " + deque.getFirst());
        System.out.println("Last element: " + deque.getLast());
        System.out.println(deque);
        System.out.println("");System.out.println("");System.out.println("");

        System.out.println("Removing first element: " + deque.removeFirst());
        System.out.println("Removing last element: " + deque.removeLast());
        System.out.println(deque);
        System.out.println("");System.out.println("");System.out.println("");

        System.out.println("Size after removals: " + deque.size());
        System.out.println("First element after removals: " + deque.getFirst());
        System.out.println("Last element after removals: " + deque.getLast());
        System.out.println(deque);
        System.out.println("");System.out.println("");System.out.println("");
    }
}