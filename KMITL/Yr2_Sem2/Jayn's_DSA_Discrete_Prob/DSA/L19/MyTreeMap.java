public class MyTreeMap<K extends Comparable<K>, V> {

    private Node root;

    private class Node {
        private K key;
        private V value;
        private Node left, right;

        public Node(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    public V get(K k) {
        Node node = get(root, k);
        return (node == null) ? null : node.value;
    }

    private Node get(Node x, K k) {
        if (x == null) return null;

        int cmp = k.compareTo(x.key);
        if (cmp < 0) return get(x.left, k);
        else if (cmp > 0) return get(x.right, k);
        else return x;
    }

    public void put(K k, V v) {
        root = put(root, k, v);
    }

    private Node put(Node x, K k, V v) {
        if (x == null) return new Node(k, v);

        int cmp = k.compareTo(x.key);
        if (cmp < 0) x.left = put(x.left, k, v);
        else if (cmp > 0) x.right = put(x.right, k, v);
        else x.value = v;

        return x;
    }

    public K lowerKey(K k) {
        Node lowerNode = lowerKey(root, k);
        return (lowerNode == null) ? null : lowerNode.key;
    }

    private Node lowerKey(Node x, K k) {
        if (x == null) return null;

        int cmp = k.compareTo(x.key);

        if (cmp <= 0) return lowerKey(x.left, k);

        Node lowerRight = lowerKey(x.right, k);

        return (lowerRight != null) ? lowerRight : x;
    }

    public void printInOrder() {
        printInOrder(root);
    }

    private void printInOrder(Node x) {
        if (x == null) return;

        printInOrder(x.left);
        System.out.println(x.key + " " + x.value);
        printInOrder(x.right);
    }

    // Additional methods and utility functions can be added as needed

    // Example usage:
    public static void main(String[] args) {
        MyTreeMap<Integer, String> treeMap = new MyTreeMap<>();
        treeMap.put(3, "Three");
        treeMap.put(1, "One");
        treeMap.put(5, "Five");
        treeMap.put(2, "Two");
        treeMap.put(4, "Four");

        //      3

        //  1       5

        //    2   4

        System.out.println("Value for key 2: " + treeMap.get(2));
        System.out.println("Lower key for 3: " + treeMap.lowerKey(3));
        treeMap.printInOrder();
    }
}
