import java.util.*;

public class RecursivePal<T> {
    public boolean isRecursivePalindrome(T[] a) {
        boolean first_half;
        boolean whole_array;
        int n = a.length;

        if (n <= 1) return true;

        else {
            T[] reversed_a = Arrays.copyOfRange(a, 0, n);
            Collections.reverse(Arrays.asList(reversed_a));
            whole_array = Arrays.equals(a, reversed_a);

            T[] left = Arrays.copyOfRange(a, 0, n / 2);
            first_half = isRecursivePalindrome(left);
        }
        return (first_half && whole_array);
    }
    public static void main(String[] args) {
        Integer[] a0 = {1, 1, 5, 1, 1};
        Integer[] a1 = {7, 8, 7, 7, 8, 7};
        Integer[] a2 = {2, 0, 4, 0, 2};
        Integer[] a3 = {7, 4, 5, 5, 4, 7, 9, 7, 4, 5, 5, 4, 7};

        System.out.println(new RecursivePal<>().isRecursivePalindrome(a0));
        System.out.println(new RecursivePal<>().isRecursivePalindrome(a1));
        System.out.println(new RecursivePal<>().isRecursivePalindrome(a2));
        System.out.println(new RecursivePal<>().isRecursivePalindrome(a3));
    }
}
