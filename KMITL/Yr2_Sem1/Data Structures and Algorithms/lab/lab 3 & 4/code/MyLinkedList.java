package code;

public class MyLinkedList {
    public static class Node{
        int data;
        Node next;
        public Node(){
            data = 0;
            next = null;
        }
        public Node(int d){
            data = d;
        }
    }


Node head = null;

public String toString(){
    StringBuffer sb = new StringBuffer("head");
    Node p = head;
    while(p!=null){
        sb.append("-->[");
        sb.append(p.data);
        sb.append("]");
        p = p.next;
    }
    sb.append("-> null");
    return new String(sb);
}

public int getAt(int i) {
    Node p = head;
    while(i>0) {
        p = p.next;
        i--;
    }
    return p.data;
}

public void setAt(int d, int i) {
    Node p = head;
    while(i>0) {
        p = p.next;
        i--;
    }
    p.data = d;
}

public void add(int d){
    Node p = new Node(d);
    p.next = head;
    head = p;
}

public void add(int [] d){
    for(int i=d.length-1; i>=0; i--){
        add(d[i]);
    }
}

public void insert(int d){
    Node p = head;
    Node q = null;
    while(p!=null && p.data<d){
        q = p;
        p = p.next;
    }
    Node t = new Node(d);
    t.next = p;
    if(q==null){
        head = t;
    }else{
        q.next = t;
    }

    
}
public void insert(int [] d){
    for(int i=d.length-1; i>=0; i--){
        insert(d[i]);
    }
}

public void append(int d) {
    Node p = head;
    while(p.next!=null) {
        p = p.next;
    }
    Node q = new Node(d);
    p.next = q;
}

public int find(int d) {
    Node p = head;
    int count = 0;
    while(p!=null) {
        if(p.data==d) {
            return count;
        }
        p = p.next;
        count++;
    }
    return -1;
}

private int size(){
    int count = 0;
    Node p = head;
    while(p!=null){
        count++;
        p = p.next;
    }
    return count;
}

public void delete(int d) {
    Node t = new Node(0);
    t.next = head;
    Node p = t;
    while( (p.next!=null) && (p.next.data!=d) ) {
        p = p.next;
    }
    if(p.next!=null) {
        p.next = p.next.next;
    }
    head = t.next;
}

public void q1_rotate_clockwise(int k){
    int n = size();
    k = k%n;
    System.out.println("k = " + k);
    if(k==0) return;
    Node p = head;
    while(k>1) {
        // System.out.println("p.data = " + p.data);
        p = p.next;
        k--;
    }
    Node q = p.next;
    p.next = null;
    p = q;
    while(p.next!=null) {
        p = p.next;
    }
    p.next = head;
    head = q;
}

public void q2_reverse(){
    Node p = head;
    Node q = null;
    while(p!=null) {
        Node t = p.next;
        p.next = q;
        q = p;
        p = t;
    }
    head = q;
}

public void q3_remove_dup(){
    Node p = head;
    while(p!=null) {
        Node q = p;
        while(q.next!=null) {
            if(q.next.data==p.data) {
                q.next = q.next.next;
            } else {
                q = q.next;
            }
        }
        p = p.next;
    }
}

public void q4_increment_digits(){
    Node p = head;
    Node q = null;
    while(p!=null) {
        if(p.data!=9) {
            q = p;
        }
        p = p.next;
    }
    if(q==null) {
        Node t = new Node(1);
        t.next = head;
        head = t;
        q = head;
    } else {
        q.data++;
        q = q.next;
    }
    while(q!=null) {
        q.data = 0;
        q = q.next;
    }
}

public boolean q5_isPalindrome(){
    Node p = head;
    Node q = null;
    while(p!=null) {
        Node t = new Node(p.data);
        t.next = q;
        q = t;
        p = p.next;
    }
    p = head;
    while(p!=null) {
        if(p.data!=q.data) {
            return false;
        }
        p = p.next;
        q = q.next;
    }
    return true;
}

}
