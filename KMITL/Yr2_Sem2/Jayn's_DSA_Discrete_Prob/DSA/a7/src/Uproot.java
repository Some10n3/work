import java.util.HashMap;
import java.util.Map;

public class Uproot {

    public static HashMap<Integer, Integer> treeToParentMap(BinaryTreeNode T) {
        HashMap<Integer, Integer> parentMap = new HashMap<>();
        populateParentMap(T, null, parentMap);
        return parentMap;
    }

    private static void populateParentMap(BinaryTreeNode node, Integer parentKey, HashMap<Integer, Integer> parentMap) {
        if (node != null) {
            parentMap.put(node.key, parentKey);
            populateParentMap(node.left, node.key, parentMap);
            populateParentMap(node.right, node.key, parentMap);
        }
    }

    public static BinaryTreeNode parentMapToTree(Map<Integer, Integer> map) {
        if (map == null || map.isEmpty()) {
            return null;
        }

        Map<Integer, BinaryTreeNode> nodeMap = new HashMap<>();
        BinaryTreeNode root = null;

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            Integer key = entry.getKey();
            Integer parentKey = entry.getValue();

            BinaryTreeNode node = nodeMap.getOrDefault(key, new BinaryTreeNode(key));
            if (parentKey == null) {
                root = node;
            } else {
                BinaryTreeNode parent = nodeMap.getOrDefault(parentKey, new BinaryTreeNode(parentKey));
                if (parent.left == null) {
                    parent.left = node;
                } else {
                    parent.right = node;
                }
                nodeMap.put(parentKey, parent);
            }
            nodeMap.put(key, node);
        }

        return root;
    }

    public static void main(String[] args) {
        // Example usage:
        BinaryTreeNode root = new BinaryTreeNode(
                new BinaryTreeNode(new BinaryTreeNode(14), 20, null),
                1,
                new BinaryTreeNode(new BinaryTreeNode(2), 9, new BinaryTreeNode(18))
        );

        HashMap<Integer, Integer> parentMap = treeToParentMap(root);
        System.out.println("Parent Mapping:");
        for (Map.Entry<Integer, Integer> entry : parentMap.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }

        BinaryTreeNode newRoot = parentMapToTree(parentMap);
        System.out.println("\nBinary Tree from Parent Mapping:");
        printTree(newRoot);
    }

    // Utility function to print binary tree (inorder traversal)
    public static void printTree(BinaryTreeNode node) {
        if (node == null) return;
        printTree(node.left);
        System.out.print(node.key + " ");
        printTree(node.right);
    }
}
