import java.util.Stack;

class Lecture18 {

    static class TreeNode<E> {
        E key;
        TreeNode<E> left, right;
    }

    public static int count(TreeNode<?> tree) {
        if (tree == null) {
            return 0;
        }
        return 1 + count(tree.left) + count(tree.right);
    }

    public static String concatPreorder(TreeNode<String> tree) {
        if (tree == null) {
            return "";
        }

        StringBuilder result = new StringBuilder();
        Stack<TreeNode<String>> stack = new Stack<>();
        stack.push(tree);

        while (!stack.isEmpty()) {
            TreeNode<String> current = stack.pop();
            result.append(current.key);

            // Push right child first to ensure left child is processed first (since it's a stack)
            if (current.right != null) {
                stack.push(current.right);
            }
            if (current.left != null) {
                stack.push(current.left);
            }
        }

        return result.toString();   
    }

    public static void main(String[] args) {
        // Example usage
        TreeNode<String> root = new TreeNode<>();
        root.key = "A";
        root.left = new TreeNode<>();
        root.left.key = "C";
        root.left.left = new TreeNode<>();
        root.left.left.key = "D";
        root.right = new TreeNode<>();
        root.right.key = "B";
        root.right.left = new TreeNode<>();
        root.right.left.key = "E";
        root.right.right = new TreeNode<>();
        root.right.right.key = "F";

        System.out.println("Number of nodes: " + count(root));
        System.out.println("Concatenated Pre-order traversal: " + concatPreorder(root));
    }
}
