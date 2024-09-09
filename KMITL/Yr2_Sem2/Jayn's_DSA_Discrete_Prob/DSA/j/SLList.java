public class SLList {
    private static class IntNode {
        int head;
        IntNode next;
        public IntNode(int h, IntNode r) {
            this.head = h;
            this.next = r;
        }
    }
    private IntNode first;
    private int s = 0;

    public SLList() {
        first = null;
    }

    public SLList(int x) {
        first = new IntNode(x, null);
    }

    public void addFirst(int x) {
        first = new IntNode(x, first);
        s++;
    }

    public int getFirst() {
        return first.head;
    }

    public int size(){
        return s;
    }

    public void addLast(int x) {
        s += 1;
        if (first == null) {
            first = new IntNode(x, null);
            return;
        }
        IntNode p = first;
        while (p.next != null) {
            p = p.next;
        }
        p.next = new IntNode(x, null);
    }

    public int getLast(){
        if (first == null) {
            throw new IllegalArgumentException("List is empty");
        }
        IntNode p = first;
        while (p.next != null) {
            p = p.next;
        }
        return p.head;
    }

    public String toString(){
        String a = "[ ";
        IntNode b = first;
        while (b != null){
            a += b.head;
            if (b.next != null){
                a += " -> ";
            }
            else{
                a += " -> null";
            }
            b = b.next;

        }
        a += " ]";
        return a;
    }

    public void removeFirst(){
        if (first == null) {
            return;
        }
        first = first.next;
        s--;
    }

    // int head
    // IntNode next

    // set first to first.next to remove the first node
    // [ 0 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> null ]  
    // 
    // [ 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> null ]
    // 

    public void insert(int newValue, int k){
        if (k == 0){
            addFirst(newValue);
            return;
        }
        IntNode p = first;
        while (k > 1 && p != null){
            p = p.next;
            k--;
        }
        // newValue = 11

        // k = 3

        // [ 0 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> null ]  

        // [ 0 -> 2 -> 3 -> 11 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> null ]

        if (p == null){
            throw new IllegalArgumentException("List is too short");
        }
        p.next = new IntNode(newValue, p.next);
        s++;
    }


}

class main {
    public static void main(String args[]){
        SLList a = new SLList();
        a.addLast(1);
        a.addLast(2);
        a.addLast(3);
        a.addLast(4);
        a.addLast(5);
        a.addLast(6);
        a.addLast(7);
        a.addLast(8);
        a.addLast(9);
        a.addLast(10);

        System.out.println("#----------------#");
        System.out.println(a);
        System.out.println("size : " + a.size());
        System.out.println("last node : " + a.getLast());
        a.removeFirst();
        System.out.println("#----------------#");
        System.out.println(a);
        System.out.println("size : " + a.size());
        System.out.println("last node : " + a.getLast());
        a.addFirst(0);
        System.out.println("#----------------#");
        System.out.println(a);
        System.out.println("size : " + a.size());
        System.out.println("last node : " + a.getLast());
        a.insert(11, 10);
        System.out.println("#----------------#");
        System.out.println(a);
        System.out.println("size : " + a.size());
        System.out.println("last node : " + a.getLast());


    }
}