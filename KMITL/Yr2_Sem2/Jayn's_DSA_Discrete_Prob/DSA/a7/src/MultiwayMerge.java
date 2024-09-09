import java.util.LinkedList;
import java.util.PriorityQueue;

public class MultiwayMerge {
    public static void main(String[] args) {
        // Sample input: k linked lists
        LinkedList<Integer>[] lists = new LinkedList[3];

        // List 1: 1 -> 3 -> 5
        lists[0] = new LinkedList<>();
        lists[0].add(1);
        lists[0].add(3);
        lists[0].add(5);

        // List 2: 2 -> 4 -> 6
        lists[1] = new LinkedList<>();
        lists[1].add(2);
        lists[1].add(4);
        lists[1].add(6);

        // List 3: 0 -> 7 -> 8
        lists[2] = new LinkedList<>();
        lists[2].add(0);
        lists[2].add(7);
        lists[2].add(8);

        // Merging lists
        LinkedList<Integer> mergedList = mergeAll(lists);

        // Output the merged list
        System.out.println("Merged List: " + mergedList);
    }

    public static LinkedList<Integer> mergeAll(LinkedList<Integer>[] lists) {
        // Create a priority queue to store lists
        PriorityQueue<LinkedList<Integer>> pq = new PriorityQueue<>((list1, list2) -> list1.peek() - list2.peek());

        // Add all lists to the priority queue
        for (LinkedList<Integer> list : lists) {
            if (!list.isEmpty()) {
                pq.add(list);
            }
        }

        // Merge the lists
        LinkedList<Integer> mergedList = new LinkedList<>();
        while (!pq.isEmpty()) {
            LinkedList<Integer> smallestList = pq.poll();
            mergedList.add(smallestList.poll());

            // If the list still has elements, put it back in the priority queue
            if (!smallestList.isEmpty()) {
                pq.add(smallestList);
            }
        }

        return mergedList;
    }
}
