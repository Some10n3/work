
import code.BST;
import code.TreeNode;

public class main {
    public static void main(String[] args) {
        demo12();
        System.out.println("Done!");
        // demo1();
    }

    public static void demo12() {
        int [] data = {2,1,3,4,5,6,7,8,9};

        //    2
        //   1 3
        //      4
        //       5
        //        6
        //         7
        //          8
        //           9

        BST bst = new BST();
        for (int j = 0; j < data.length; j++)
        bst.insert(data[j]);
        bst.printInOrder();
        System.out.println("Tree height = " + bst.height());

        int[] dat = { 15, 20, 10, 18, 16, 12, 8, 25, 19, 30};

        //        15
        //   10         20
        //  8 12     18   25
        //         16 19    30

        bst = new BST();
        for (int j = 0; j < dat.length; j++)
        bst.insert(dat[j]);
        bst.printInOrder();
       System.out.println("Tree height = " + bst.height());
        demo22(bst);
    }

    public static void demo22(BST bst) {
        System.out.println("node with max value " + bst.findMaxFrom(bst.getRoot()));
        demo33(bst);
    }

    public static void demo33(BST bst) {
        bst.delete(12, bst.getRoot());
        System.out.println(bst.search(20)); // 18<-20->25
        System.out.println(bst.search(25)); // null<-25->30
        System.out.println(bst.search(16)); // null<-16->null
        System.out.println(bst.search(10)); // 8<-10->null
        System.out.println(bst.search(12)); // not found
    }

    public static void demo1() { 
        System.out.println("-insert and preOrder traversal-"); int[] dat = { 15, 20, 10, 18, 16, 12, 8, 25, 19, 30 };
        BST bst = new BST();
        for (int j = 0; j < dat.length; j++) 
        bst.insert(dat[j]);
        bst.printPreOrder(); // 15 10 8 12 20 18 16 19 25 30 
        System.out.println(); 
        
        demo2(bst);
    }

    //uncomment demo2() invocation inside demo1() 
    static void demo2(BST bst) { 
        System.out.println("-more traversal---"); 
        
        bst.printInOrder(); 
        System.out.println(); // 8 10 12 15 16 18 19 20 25 30
        
        bst.printPostOrder(); 
        System.out.println();// 8 12 10 16 19 18 30 25 20 15 
        
        demo3(bst);
    }

    //uncomment demo3() invocation inside demo2()
    static void demo3(BST bst){
        System.out.println("-search recursive---"); 
        System.out.println(bst.search(20)); // 18<-20->25 
        System.out.println(bst.search(25)); // null<-25->30 
        System.out.println(bst.search(12)); // null<-12->null 
        System.out.println(bst.search(1)); // null 
        System.out.println(bst.searchRecurse(10, bst.getRoot())); //if searchRecurse and getRoot is available
        System.out.println("-search iterative---"); 
        System.out.println(bst.searchIter(20)); 
        System.out.println(bst.searchIter(25)); 
        System.out.println(bst.searchIter(12));
        System.out.println(bst.searchIter(1));
    }
}