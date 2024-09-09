import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class KDeques {

    public static void main(String[] args) {
        List<Deque<Integer>> theDeques = new ArrayList<>();
        int x = 9;
        Deque<Integer> deque = new ArrayDeque<>();
        deque.add(6);
        deque.add(3);
        deque.add(1);

        Deque<Integer> deque2 = new ArrayDeque<>();
        deque2.add(9);
        deque2.add(5);
        deque2.add(2);
        deque2.add(1);

        Deque<Integer> deque3 = new ArrayDeque<>();
        deque3.add(4);
        deque3.add(1);

        theDeques.add(deque);
        theDeques.add(deque2);
        theDeques.add(deque3);

        // theDeques.forEach(d -> {
        //     System.out.println("Deque: ");
        //     d.forEach(System.out::println);
        // });

        // System.out.println(deque.peekLast());

        int score = maximizeScore(theDeques, x);
        System.out.println("Score: " + score);
    }

    public static int maximizeScore(List<Deque<Integer>> theDeques, int x){
        int score = 0;
        int sum = 0;
        int least = -1;
        int dequeIndex = -1;

        while (sum <= x) {
            least = Integer.MAX_VALUE; // Reset least for each iteration
            dequeIndex = -1; // Reset dequeIndex for each iteration
            
            // Find the deque with the smallest last element
            for (int i = 0; i < theDeques.size(); i++) {
                Deque<Integer> deque = theDeques.get(i);
                if (!deque.isEmpty() && (deque.peekLast() < least || dequeIndex == -1)) {
                    least = deque.peekLast();
                    dequeIndex = i;
                }
            }
        
            // All deques are empty
            if (dequeIndex == -1) {
                break;
            }
            
            sum += least;
            theDeques.get(dequeIndex).removeLast();
            if (sum <= x){
                score++;
            }
        }
        


        return score;
    }

}
