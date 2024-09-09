import java.util.ArrayDeque;

public class ArrayDequeExample {
    public static void main(String[] args) {
        // Creating an ArrayDeque
        ArrayDeque<String> arrayDeque = new ArrayDeque<>();

        // Adding elements to the rear
        arrayDeque.add("One");
        arrayDeque.add("Two");
        arrayDeque.add("Three");

        // Adding elements to the front
        arrayDeque.addFirst("Zero");

        // Removing elements from the rear
        String lastElement = arrayDeque.removeLast();

        // Accessing elements
        System.out.println("First Element: " + arrayDeque.getFirst());
        System.out.println("Last Element: " + arrayDeque.getLast());

        // Displaying all elements
        System.out.println("All Elements: " + arrayDeque);

        System.out.println("Size: " + arrayDeque.size());
    }
}
