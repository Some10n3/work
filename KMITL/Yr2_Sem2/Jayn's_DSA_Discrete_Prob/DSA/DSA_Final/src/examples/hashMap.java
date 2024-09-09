package examples;

import java.util.HashMap;
import java.util.Map;

public class hashMap{
    public static void main(String[] args) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        //methods : put, get, containsKey, remove, size, clear
        map.put(1, 2);
        map.put(2, 3);
        map.put(3, 4);

        System.out.println(map.get(1)); // 2

        System.out.println(map.containsKey(2)); // true

        map.remove(2);

        System.out.println(map.size()); // 2

        map.clear();

        //more methods: keySet, values, entrySet

        map.put(1, 2);
        map.put(2, 3);
        System.out.println(map.keySet()); // [1, 2]

        System.out.println(map.values()); // [2, 3]

        System.out.println(map.entrySet()); // [1=2, 2=3]

        //Iterating through a map

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        //Iterating through keys

        for (Integer key : map.keySet()) {
            System.out.println(key);
        }

        //Iterating through values

        for (Integer value : map.values()) {
            System.out.println(value);
        }

        //Iterating through keys and values

        for (Integer key : map.keySet()) {
            System.out.println(key + " " + map.get(key));
        }

        //Iterating through keys and values using forEach

        map.forEach((key, value) -> {
            System.out.println(key + " " + value);
        });

        //Iterating through keys using forEach

        map.keySet().forEach(key -> {
            System.out.println(key);
        });

        //Iterating through values using forEach

        map.values().forEach(value -> {
            System.out.println(value);
        });

        //Iterating through keys and values using forEach

        map.entrySet().forEach(entry -> {
            System.out.println(entry.getKey() + " " + entry.getValue());
        });

    }
         
}