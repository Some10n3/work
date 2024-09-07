//Chanasorn Howattanakulphong    65011277

package code;
import java.util.*;

public class BST { 
    TreeNode root; 
    public BST() { root = null; }
    public TreeNode getRoot() {
        return root;
    }
    public void insert(int d) { 
        if (root == null) {
            root = new TreeNode(d); 
        }   
        else {
            TreeNode cur = root; 
            while (cur != null) { 
                if (d < cur.getData()) {
                    if (cur.getLeft() != null) cur = cur.getLeft();
                    else { /* your code 1*/ 
                        cur.left = new TreeNode(d); 
                        cur.left.parent = cur; 
                        return;
                    }
                } 
                else { //! (d < p.data) 
                    if (cur.getRight() != null) {/* your code 2*/;
                        cur = cur.getRight(); 
                    }
                    else {
                        cur.right = new TreeNode(d); 
                        cur.right.parent = cur; 
                        return;
                    } 
                } 
            } 
        } 
    }

    public void printPreOrder() { 
        printPreOrderRecurse(root);
    }

    public void printInOrder() { 
        printInOrderRecurse(root);
    } 
    
    public void printPostOrder() { 
        printPostOrderRecurse(root);
    }
    
    private void printPreOrderRecurse(TreeNode node) { /* your code 3*/
        if (node == null) return;
        System.out.print(node.getData() + " ");
        printPreOrderRecurse(node.getLeft());
        printPreOrderRecurse(node.getRight());
    }

    private void printInOrderRecurse(TreeNode node) { /* your code 4*/ 
        if (node == null) return;
        printInOrderRecurse(node.getLeft());
        System.out.print(node.getData() + " ");
        printInOrderRecurse(node.getRight());        
    }

    private void printPostOrderRecurse(TreeNode node) { /* your code 5*/
        if (node == null) return;
        printPostOrderRecurse(node.getLeft());
        printPostOrderRecurse(node.getRight());
        System.out.print(node.getData() + " ");
    }

    public TreeNode search(int d) { 
        TreeNode result = searchRecurse(d, root); 
        return result;
    }
    public TreeNode searchRecurse(int d, TreeNode n) { 
        if (n == null) return null; 
        if (d == n.data) return n; /* your code 7*/
        else
        if (d < n.data) return searchRecurse(d, n.left);
        else
        return searchRecurse(d, n.right);
    }

    public TreeNode searchIter(int key) { 
        if (root.data == key) return root;
        TreeNode current = root; 
        while (current != null) { 
            if (key < current.data) { 
                if (current.left != null) current = current.left;
            } 
            else {
                if (current.right != null) current = current.right;
            }
            if (current.data == key) return current;
        }
        /* your code 8 */
        return null;
    }

    public int height() {
        return root == null ? 0 : height(root);
    }
    public int height(TreeNode node) {
        if (node == null)
        return 0;
        return 1 + Math.max(height(node.left), height(node.right));
    }

    public TreeNode findMaxFrom(TreeNode subtreeHead) {
        TreeNode current = subtreeHead;
        while (current.right != null) {
            current = current.right;
        }

        return current;
    }

    public void delete(int d, TreeNode current) { 
        if (current == null) return; //not found 
        if (d < current.data) delete(d, current.left); 
        else if (d > current.data) delete(d, current.right); 
        else { //found ... time to delete
            if (current.left == null || current.right == null) { // 0 or 1 child 
                TreeNode q = (current.left == null) ? current.right : current.left; 
                if (current.parent.left == current)
                current.parent.left = q; //this node is left child 
                else current.parent.right = q;
                if (q != null) q.parent = current.parent; 
                System.out.println("Deleted " + d);                
            }
            else { // two children
                TreeNode q = findMaxFrom(current.left);
                // * your code 11 * //
                current.data = q.data; //copy the data
                delete(q.data, current.left); //delete the node that had the max value
            } // two children } //found
        }
    }

}