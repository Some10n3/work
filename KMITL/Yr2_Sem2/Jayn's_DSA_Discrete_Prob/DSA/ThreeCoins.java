import java.util.ArrayList;
import java.util.List;

public class ThreeCoins {
    public static List<Integer> change(int n) {
        // Theorem: Any amount of n-cents, where n >= 20, can be formed using 5, 11, and 12-cent stamps.
    
        // Base cases
        if (n == 20) {
            return List.of(5, 5, 5, 5);
        }
        if (n == 21) {
            return List.of(5, 5, 11);
        }
        if (n == 22) {
            return List.of(5, 5, 12);
        }
        if (n == 23) {
            return List.of(11, 12);
        }
        if (n == 24) {
            return List.of(12, 12);
        }
    
        // Inductive step
        List<Integer> temp = new ArrayList<>(change(n - 5));
        temp.add(5);
    
        return temp;
        /*
        Explaining the inductive step:
    
        For n >= 25, we observe that n-cents can be made by adding a 5-cent stamp to (n - 5)-cents.
        We use the inductive hypothesis that (n - 5)-cents can be formed using 5, 11, and 12-cent stamps.
    
        Therefore, n-cents can be formed by extending the solution for (n - 5)-cents with an additional 5-cent stamp.
    
        By repeating this process, we can prove that any amount of n-cents, where n >= 20, can be formed using 5, 11, and 12-cent stamps.
         */
    }
    public static void main(String[] args){
        System.out.println(change(25));  // [5, 5, 5, 5, 5]
        System.out.println(change(26));  // [5, 5, 11, 5]
        System.out.println(change(27));  // [5, 5, 12, 5]
        System.out.println(change(28));  // [11, 12, 5]
        System.out.println(change(29));  // [12, 12, 5]
        System.out.println(change(30));  // [5, 5, 5, 5, 5, 5]
    }
}


    // public static void main(String[] args){
    //     System.out.println(change(25));  // [5, 5, 5, 5, 5]
    //     System.out.println(change(26));  // [5, 5, 11, 5]
    //     System.out.println(change(27));  // [5, 5, 12, 5]
    //     System.out.println(change(28));  // [11, 12, 5]
    //     System.out.println(change(29));  // [12, 12, 5]
    //     System.out.println(change(30));  // [5, 5, 5, 5, 5, 5]
    // }
    // public static void main(String[] args) {
    //     System.out.println(change(25)); //returns [5, 5, 5, 5, 5]
    //     System.out.println(change(26)); //returns [11, 5, 5, 5]
    //     System.out.println(change(27)); //returns [11, 11, 5]
    //     System.out.println(change(28)); //returns [12, 11, 5]
    //     System.out.println(change(6)); //returns 
    // }

    // //there's 5, 11, 12 cents stamps. returns the minimum number of stamps to make n cents
    // public static List<Integer> change(int n) {
    //     //recursive base case
    //     if (n == 0) {
    //         return new ArrayList<Integer>();
    //     }

    //     //recursive case
    //     List<Integer> best = null;
    //     int[] coins = {5, 11, 12};
    //     for (int i = 0; i < coins.length; i++) {
    //         int coin = coins[i];
    //         if (n - coin >= 0) {
    //             List<Integer> temp = change(n - coin);
    //             if (temp == null) {
    //                 continue;//skip this iteration
    //             }
    //             temp.add(coin);
    //             if (best == null || temp.size() < best.size()) {
    //                 best = temp;
    //             }
    //         }
    //     }
    //     return best;
    // }