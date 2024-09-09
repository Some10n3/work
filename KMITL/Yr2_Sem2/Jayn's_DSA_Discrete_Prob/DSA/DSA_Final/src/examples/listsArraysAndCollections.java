package examples;

import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.util.Arrays;

public class listsArraysAndCollections {
    
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        
        //methods : add, get, set, remove, size, clear
        list.add(1);
        list.add(2);
        list.add(3);
        
        System.out.println(list.get(1)); // 2
        
        list.set(1, 4);
        
        System.out.println(list.get(1)); // 4
        
        list.remove(1);
        
        System.out.println(list.size()); // 2
        
        list.clear();
        
        //more methods: addAll, contains, indexOf, lastIndexOf, isEmpty, subList
        
        list.addAll(Arrays.asList(1, 2, 3));
        
        System.out.println(list.contains(1)); // true
        
        System.out.println(list.indexOf(2)); // 1
        
        System.out.println(list.lastIndexOf(3)); // 2
        
        System.out.println(list.isEmpty()); // false
        
        List<Integer> subList = list.subList(1, 3);
        
        System.out.println(subList); // [2, 3]
        
        //Iterating through a list
        
        list.forEach(i -> {
            System.out.println(i);
        });
        
        //Sorting a list
        
        List<Integer> unsortedList = Arrays.asList(3, 1, 2);
        
        Collections.sort(unsortedList);
        
        System.out.println(unsortedList); // [1, 2, 3]

        //Reversing a list

        List<Integer> reversedList = Arrays.asList(1, 2, 3);

        Collections.reverse(reversedList);

        System.out.println(reversedList); // [3, 2, 1]

        //Shuffling a list

        List<Integer> shuffledList = Arrays.asList(1, 2, 3);

        Collections.shuffle(shuffledList);

        System.out.println(shuffledList); // [2, 3, 1]

        //Swapping elements in a list

        List<Integer> swappedList = new ArrayList<>(Arrays.asList(1, 2, 3));

        Collections.swap(swappedList, 0, 2);

        System.out.println(swappedList); // [3, 2, 1]

        //Rotating elements in a list

        List<Integer> rotatedList = new ArrayList<>(Arrays.asList(1, 2, 3));

        Collections.rotate(rotatedList, 1);

        System.out.println(rotatedList); // [3, 1, 2]

        //Filling elements in a list

        List<Integer> filledList = new ArrayList<>(Arrays.asList(1, 2, 3));

        Collections.fill(filledList, 0);

        System.out.println(filledList); // [0, 0, 0]

        //Copying elements from one list to another

        List<Integer> sourceList = Arrays.asList(1, 2, 3);

        List<Integer> destinationList = new ArrayList<>(Arrays.asList(4, 5, 6));

        Collections.copy(destinationList, sourceList);

        System.out.println(destinationList); // [1, 2, 3]

        //Replacing elements in a list

        List<Integer> replacedList = new ArrayList<>(Arrays.asList(1, 2, 3));

        Collections.replaceAll(replacedList, 2, 4);

        System.out.println(replacedList); // [1, 4, 3]

        //Checking for disjoint elements in two lists

        List<Integer> firstList = Arrays.asList(1, 2, 3);

        List<Integer> secondList = Arrays.asList(4, 5, 6);

        boolean disjoint = Collections.disjoint(firstList, secondList);

        System.out.println(disjoint); // true

        //Finding the frequency of an element in a list

        List<Integer> frequencyList = Arrays.asList(1, 2, 3, 1, 2, 3, 1, 2, 3);

        int frequency = Collections.frequency(frequencyList, 1);

        System.out.println(frequency); // 3

        //Finding the minimum and maximum elements in a list

        List<Integer> minMaxList = Arrays.asList(3, 1, 2);

        int min = Collections.min(minMaxList);

        int max = Collections.max(minMaxList);

        System.out.println(min); // 1

        System.out.println(max); // 3

    }
}
