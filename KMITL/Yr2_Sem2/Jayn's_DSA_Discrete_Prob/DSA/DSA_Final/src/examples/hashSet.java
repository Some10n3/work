package examples;

import java.util.HashSet;


public class hashSet {

    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();
        
        // elements in HashSet are unique

        //methods : add, contains, remove, size, clear
        set.add(1);
        set.add(2);
        set.add(3);

        System.out.println(set.contains(1)); // true

        set.remove(2);

        System.out.println(set.size()); // 2

        set.clear();

        //more methods: iterator

        set.add(1);
        set.add(2);
        System.out.println(set.iterator()); // java.util.HashMap$KeyIterator@2a139a55

        //Iterating through a set

        for (Integer i : set) {
            System.out.println(i);
        }

        //Iterating through a set using forEach

        set.forEach(i -> {
            System.out.println(i);
        });
    }
}
