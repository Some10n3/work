import java.util.PriorityQueue;

public class Sweet {
    public static double superSweet(long k, long[] sweetness) {
        PriorityQueue<Long> minHeap = new PriorityQueue<>();

        // Initialize the priority queue with sweetness values
        for (long sweet : sweetness) {
            //minHeap.offer() adds the element to the queue
            //if the element is less than the head of the queue, it becomes the head
            //the minheap is sorted in ascending order
            minHeap.offer(sweet);
        }

        //minHeap.peek() returns the head of the queue
        //minHeap.poll() removes the head of the queue
        while (minHeap.size() >= 2 && minHeap.peek() < k) {
            long leastSweet = minHeap.poll();
            long secondLeastSweet = minHeap.poll();
            long newSweetness = leastSweet + (2 * secondLeastSweet); //Formula fromt the problem
            minHeap.offer(newSweetness);
        }

        // Check if every item is at least as sweet as k
        for (long sweet : minHeap) {
            if (sweet < k) {
                return Double.NaN;
            }
            
        }

        // Compute the average sweetness
        double sum = 0;
        for (long sweet : minHeap) {
            sum += sweet;
        }
        return sum / minHeap.size();
    }

    public static void main(String[] args) {
        System.out.println(superSweet(7, new long[]{1, 12, 3, 9, 2, 10})); // Output: 11.0
        System.out.println(superSweet(7, new long[]{7})); // Output: 7.0
        System.out.println(superSweet(7, new long[]{1, 2})); // Output: NaN
    }
}
