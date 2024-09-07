package code; 
public class TreeNode { 
    int data;
    TreeNode left, right, parent;
    
    public TreeNode(int d) { 
        data = d;
    } 

    public int getData() {
        return data;
    }

    public TreeNode getLeft() {
        return left;
    }

    public TreeNode getRight() {
        return right;
    }

    public TreeNode getParent() {
        return parent;
    }

    @Override
    public String toString() { 
        /* your code 6 */
        // There are 4 cases 
        // 1. left != null && right != null
        if (left != null && right != null) 
        return left.data + "<-" + data + "->" + right.data; 
        
        // 2. left != null && right == null
        else if (left != null) 
        return left.data + "<-" + data + "->null"; 
        
        // 3. left == null && right != null
        else if (right != null) 
        return "null<-" + data + "->" + right.data; 
        
        // 4. left == null && right == null
        else 
        return "null<-" + data + "->null";
    } 
}