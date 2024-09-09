import java.util.Arrays;

public class MakeTree {

    public static BinaryTreeNode buildBST(int[] keys) {
        if (keys == null || keys.length == 0) {
            return null;
        }
        Arrays.sort(keys); // Sort the keys
        return buildBST(keys, 0, keys.length - 1);
    }

    private static BinaryTreeNode buildBST(int[] keys, int start, int end) {
        if (start > end) {
            return null;
        }

        int mid = (start + end) / 2;
        BinaryTreeNode root = new BinaryTreeNode(keys[mid]);
        
        root.left = buildBST(keys, start, mid - 1);
        root.right = buildBST(keys, mid + 1, end);

        return root;
    }

    public static void main(String[] args) {
        // Example usage:
        int[] keys = {7, 2, 5, 4, 1, 6, 3};
        BinaryTreeNode root = buildBST(keys);

        // Print the constructed BST (inorder traversal)
        System.out.println("Inorder traversal of constructed BST:");
        printTree(root);
    }

    // Utility function to print binary tree (inorder traversal)
    public static void printTree(BinaryTreeNode node) {
        if (node == null) return;
        printTree(node.left);
        System.out.print(node.key + " ");
        printTree(node.right);
    }
}
