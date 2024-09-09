package examples;

import java.util.PriorityQueue;

public class priorityQueue {
    
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        //methods : add, offer, remove, poll, peek, element, size, clear, contains, iterator
        
        pq.add(1);
        pq.add(2);
        pq.add(3);
        
        System.out.println(pq); // [1, 2, 3]
        
        pq.offer(4);
        
        System.out.println(pq); // [1, 2, 3, 4]
        
        pq.remove();
        
        System.out.println(pq); // [2, 4, 3]
        
        pq.poll();
        
        System.out.println(pq); // [3, 4]
        
        System.out.println(pq.peek()); // 3
        
        System.out.println(pq.element()); // 3
        
        System.out.println(pq.size()); // 2
        
        pq.clear();
        
        System.out.println(pq); // []
        
        pq.add(1);
        pq.add(2);
        pq.add(3);

        System.out.println(pq.contains(1)); // true

        //Iterating through a priority queue

        for (Integer i : pq) {
            System.out.println(i);
        }
    }
}
