/*
public Siblings(HashMap<Integer, Integer> tree) {
    parentMap = new HashMap<>();

    //Using the putAll method to copy the contents of the tree to the parentMap
    parentMap.putAll(tree);

    //Manual version of the putAll method
    // for (Integer node : tree.keySet()) {
    //     parentMap.put(node, tree.get(node));
    // }
*/

import java.util.HashMap;
import java.util.Map;

public class Siblings {
    private Map<Integer, Integer> parentMap;
    //Map<u, v> -> u is v's children
    private Map<Integer, Integer> levelMap;
    //Map<u, v> -> u is at level v

    public Siblings(Map<Integer, Integer> tree) {
        parentMap = new HashMap<>(tree);
        levelMap = new HashMap<>();
        
        // Preprocess to compute levels of each node
        for (int node : tree.keySet()) {
            computeLevel(node);
        }
    }
    
    // Helper method to compute level of a node
    private int computeLevel(int node) {
        if (node == -1) return -1; // Base case: node not found
        if (levelMap.containsKey(node)) return levelMap.get(node); // Already computed
        
        int parent = parentMap.getOrDefault(node, -1);
        int level = computeLevel(parent) + 1;
        levelMap.put(node, level);
        return level;
    }
    
    // Check if two nodes are siblings
    public boolean isSibling(int u, int v) {
        return computeLevel(u) == computeLevel(v);
    }

    public static void main(String[] args) {
        // Example usage
        Map<Integer, Integer> tree = new HashMap<>();
        tree.put(2, 1);
        tree.put(3, 1);
        tree.put(4, 2);
        tree.put(5, 2);
        tree.put(6, 3);
        tree.put(7, 3);
        
        Siblings sbl = new Siblings(tree);
        System.out.println(sbl.isSibling(4, 5));  // true, siblings
        System.out.println(sbl.isSibling(4, 6));  // true, siblings
        System.out.println(sbl.isSibling(4, 1));  // false, not siblings
        System.out.println(sbl.isSibling(2, 4));  // false, not siblings

        /*
         *          1   
         *         / \
         *        2   3
         *       / \ / \
         *      4  5 6  7
         * 
         */
    }
}
