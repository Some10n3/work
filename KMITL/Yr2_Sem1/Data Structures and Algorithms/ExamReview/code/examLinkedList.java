package code;

public class examLinkedList {
    public class Node{
        double data;
        Node next;
        public Node(double d){
            data = d;
        }
    }
    Node head;
    int currentSize;
    public examLinkedList(){
        head = null;
        currentSize = 0;
    }

    public examLinkedList(double[] arr){
        for(int i = arr.length - 1; i >= 0; i--){
            add(arr[i]);
        }
    }

    public void add(double d){
        Node p = new Node(d);
        p.next = head;
        head = p;
        currentSize++;
    }

    public void insert(double d, int index){
        Node p = head;
        Node q = null;
        while(index > 0){
            q = p;
            p = p.next;
            index--;
        }
        Node t = new Node(d);
        t.next = p;
        if(q == null){
            head = t;
        }
        else{
            q.next = t;
        }
        currentSize++;
    }

    public void setAt (int d, int i){
        Node p = head;
        while(i > 0){
            // System.out.println("p.data = " + p.data);
            p = p.next;
            i--;
        }
        // System.out.println("p.data = " + p.data);
        p.data = d;
    }
    
    public void noUnderstand () {
        Node p = head;
        int i = 3;
        while(i > 0){
            System.out.println("p.data = " + p.data);
            p = p.next;
            i--;
        }
        p.data = 10;
        System.out.println("p.data = " + p.data);
        System.out.println("head.data = " + head.data);
        System.out.println("/n");

        //loop through p
        while(p != null){
            System.out.println("p.data = " + p.data);
            p = p.next;
        }
        //loop thriough head
        while(head != null){
            System.out.println("head.data = " + head.data);
            head = head.next;
        }

    }
    
    public void q1_rotate_clockwise(int k){
        int n = currentSize;
        k = k%n;
        System.out.println("k = " + k);
        if(k==0) return;
        Node p = head;
        while(k>1) {
            System.out.println("p.data = " + p.data);
            p = p.next;
            k--;
        }
        Node q = p;
        while(q.next != null){
            System.out.println("q.data = " + q.data);
            q = q.next;
        }
        System.out.println("head.data = " + head.data);
        q.next = head;
        System.out.println("q.data = " + q.data);
        System.out.println("q.next.data = " + q.next.data);
        // printWholeList();
        head = p.next;
        // printWholeList();
        p.next = null;
    }

    public void q1Remake(int k){
        int n = currentSize;
        k = k%n;
        if(k == 0){
            return;
        }
        Node p = head;
        while(k > 1){
            p = p.next;
            k--;
        }
        // Node q = p;
        // while(q.next != null){
        //     q = q.next;
        // }
        // q.next = head;
        head = p.next;
        p.next = null;
        System.out.println("p.data = " + p.data);
    }

    public void printWholeList(){
        Node p = head;
        String listString = "";
        while(p != null){
            listString += p.data + " ";
            p = p.next;
        }
        System.out.println(listString);
    }

    public String toString(){
        Node p = head;
        String s = "";
        while(p != null){
            s += p.data + " ";
            p = p.next;
        }
        return s;
    }

}
