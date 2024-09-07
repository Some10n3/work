package code;
import code.MyQueueInterface;

public class MyPriorityQueue implements MyQueueInterface {
    int MAX_SIZE = 6;
    int heap[] = new int[MAX_SIZE];
    int size = 0;

    void swap(int a, int b) {
        heap[a] = heap[a]+heap[b];
        heap[b] = heap[a]-heap[b];
        heap[a] = heap[a]-heap[b];   
    }
    
    public void enqueue(int d) {
        if (isFull()) {
            System.out.println("Queue is full");
            return;
        }
        int p = size++;
        heap[p] = d;
        int parent = (p-1)/2;
        while( (p>0) && (heap[p]<heap[parent]) ) {
            swap(p, parent);
            p = parent;
            parent = (p-1)/2;
        }
    }
    
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return -1;
        }
        int d = heap[0];
        heap[0] = heap[--size];
        int p = 0;
        while(true) {
            int left = 2*p+1;
            if(left>=size) break; // no child
            int right = 2*p+2;
            if(right==size) { // one child
                if(heap[p]>heap[left])swap(p,left);
                break; // no more child, nothing to do
            } else { // two childs
                int q = heap[left]<heap[right]?left:right;
                if(heap[p]>heap[q]) swap(p,q);
                else break;
                    p = q;
            }
        } // end while
        return d;
    }

    public int front() {
        if (size == 0) {
            System.out.println("Heap is empty");
            return -1;
        }
        return heap[0];
    }
    
    public boolean isFull() {
        return size == MAX_SIZE;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public String toString() {
        String s = "";
        for (int i = 0; i < size; i++) {
            s += heap[i] + " ";
        }
        return s;
    }
}