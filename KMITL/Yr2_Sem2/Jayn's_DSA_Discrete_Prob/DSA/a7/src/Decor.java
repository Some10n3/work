import java.util.*;

public class Decor {
    public static BinaryTreeNode mkTree(List<Integer> postOrder, List<Integer> inOrder) {
        // Create a map to store the index of each element in the inorder list
        Map<Integer, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < inOrder.size(); i++) {
            indexMap.put(inOrder.get(i), i);
        }

        // Start the recursive construction
        return buildTree(postOrder, 0, postOrder.size() - 1,
                inOrder, 0, inOrder.size() - 1,
                indexMap);
    }

    private static BinaryTreeNode buildTree(List<Integer> postOrder, int postStart, int postEnd,
                                            List<Integer> inOrder, int inStart, int inEnd,
                                            Map<Integer, Integer> indexMap) {
        if (postStart > postEnd || inStart > inEnd) {
            return null;
        }

        // The last element in the postOrder list is the root
        int rootValue = postOrder.get(postEnd);
        BinaryTreeNode root = new BinaryTreeNode(rootValue);

        // Find the index of the root in the inorder list
        int rootIndexInInOrder = indexMap.get(rootValue);

        // Calculate the size of the left subtree
        int leftSubtreeSize = rootIndexInInOrder - inStart;

        // Recursively build left and right subtrees
        root.left = buildTree(postOrder, postStart, postStart + leftSubtreeSize - 1,
                inOrder, inStart, rootIndexInInOrder - 1,
                indexMap);
        root.right = buildTree(postOrder, postStart + leftSubtreeSize, postEnd - 1,
                inOrder, rootIndexInInOrder + 1, inEnd,
                indexMap);

        return root;
    }

    public static void main(String[] args) {
        // Example usage:
        List<Integer> postOrder = Arrays.asList(4, 5, 2, 6, 7, 3, 1);
        List<Integer> inOrder = Arrays.asList(4, 2, 5, 1, 6, 3, 7);
        BinaryTreeNode root = mkTree(postOrder, inOrder);
        // Print the constructed tree (inorder traversal)
        printInOrder(root);
    }

    public static void printInOrder(BinaryTreeNode root) {
        if (root == null) return;
        printInOrder(root.left);
        System.out.print(root.key + " ");
        printInOrder(root.right);
    }

}
