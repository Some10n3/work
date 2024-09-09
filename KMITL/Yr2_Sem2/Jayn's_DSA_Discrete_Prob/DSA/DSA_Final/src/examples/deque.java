package examples;

import java.util.Deque;
import java.util.ArrayDeque;

public class deque {
    
    public static void main(String[] args) {
        Deque<Integer> deque = new ArrayDeque<>();
        
        //methods : add, addFirst, addLast, offer, offerFirst, offerLast, remove, removeFirst, removeLast, poll, pollFirst, pollLast, element, getFirst, getLast, peek, peekFirst, peekLast, size, clear, contains, iterator
        
        deque.add(1);
        deque.add(2);
        deque.add(3);
        
        System.out.println(deque); // [1, 2, 3]
        
        deque.addFirst(0);
        deque.addLast(4);
        
        System.out.println(deque); // [0, 1, 2, 3, 4]
        
        deque.offer(5);
        deque.offerFirst(-1);
        deque.offerLast(6);
        
        System.out.println(deque); // [-1, 0, 1, 2, 3, 4, 5, 6]
        
        deque.remove();
        deque.removeFirst();
        deque.removeLast();
        
        System.out.println(deque); // [0, 1, 2, 3, 4, 5]
        
        deque.poll();
        deque.pollFirst();
        deque.pollLast();
        
        System.out.println(deque); // [1, 2, 3, 4, 5]
        
        System.out.println(deque.element()); // 1
        
        System.out.println(deque.getFirst()); // 1
        
        System.out.println(deque.getLast()); // 5
        
        System.out.println(deque.peek()); // 1
        
        System.out.println(deque.peekFirst()); // 1
        
        System.out.println(deque.peekLast()); // 5
        
        System.out.println(deque.size()); // 5
        
        deque.clear();
        
        System.out.println(deque); // []
        
        deque.add(1);
        deque.add(2);
        deque.add(3);
        
        System.out.println(deque.contains(2)); // true
        
        System.out.println(deque.iterator()); // java.util.ArrayDeque$DeqIterator@2a139a55
    }
}
