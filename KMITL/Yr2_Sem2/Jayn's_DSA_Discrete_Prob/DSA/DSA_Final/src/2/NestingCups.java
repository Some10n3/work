import java.util.HashMap;   
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;

public class NestingCups {
    public static String[] orderNestingCups(String[] measurements) {
        HashMap<Integer, String> cups = new HashMap<>();
        List<Integer> radii = new ArrayList<>();

        for (String measurement : measurements) {
            String[] parts = measurement.split(" ");
            if (Character.isDigit(parts[0].charAt(0))) {
                int radius = Integer.parseInt(parts[0]) / 2;
                cups.put(radius, parts[1]);
                radii.add(radius);
            } else {
                int radius = Integer.parseInt(parts[1]);
                cups.put(radius, parts[0]);
                radii.add(radius);
            }
        }

        Collections.sort(radii);
        // collections can be used on arraylist, list, set, map
        // ArrayList: Implements the List interface, backed by an array.
// LinkedList: Implements the List interface, backed by a doubly-linked list.
// HashSet: Implements the Set interface, stores elements in a hash table.
// TreeSet: Implements the Set interface, stores elements in a sorted tree structure.
// HashMap: Implements the Map interface, stores key-value pairs in a hash table.
// TreeMap: Implements the Map interface, stores key-value pairs in a sorted tree structure.
// LinkedHashSet

        List<String> colors = new ArrayList<>();
        for (int radius : radii) {
            colors.add(cups.get(radius));
            // System.out.println("Color : " + cups.get(radius));
            // System.out.println("Radius : " + radius);
        }

        return colors.toArray(new String[0]);
    }

    public static void main(String[] args) {
        String[] measurements = {"red 10", "10 blue", "green 7"};
        String[] orderedColors = orderNestingCups(measurements);
        System.out.println(Arrays.toString(orderedColors)); // Output: [blue, green, red]
    }
}

//Using Treemaps

// import java.util.Arrays;
// import java.util.TreeMap;
// import java.util.List;
// import java.util.ArrayList;

// public class NestingCups {
//     public static String[] orderNestingCups(String[] measurements) {
//         TreeMap<Integer, String> cups = new TreeMap<>();

//         for (String measurement : measurements) {
//             String[] parts = measurement.split(" ");
//             if (Character.isDigit(parts[0].charAt(0))) {
//                 int radius = Integer.parseInt(parts[0]) / 2;
//                 cups.put(radius, parts[1]);
//             } else {
//                 int radius = Integer.parseInt(parts[1]);
//                 cups.put(radius, parts[0]);
//             }
//         }

//         List<String> colors = new ArrayList<>(cups.values());
//         return colors.toArray(new String[0]);
//     }

//     public static void main(String[] args) {
//         String[] measurements = {"red 10", "10 blue", "green 7"};
//         String[] orderedColors = orderNestingCups(measurements);
//         System.out.println(Arrays.toString(orderedColors)); // Output: [blue, green, red]
//     }
// }
