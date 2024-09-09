public class LinkedListDeque{
    private static class IntNode<T> {
        T data;
        IntNode<T> prev;
        IntNode<T> next;

        public IntNode(T data) {
            this.data = data;
        }
    }

    private IntNode<T> first;
    private IntNode<T> last;
    private int size;

    public LinkedListDeque() {
        first = null;
        last = null;
        size = 0;
    }

    public LinkedListDeque(LinkedListDeque other) {
        first = null;
        last = null;
        size = 0;
        for (int i = 0; i < other.size(); i++) {
            addLast((T) other.get(i));
        }
    }

    public static void main(String[] args){

        LinkedListDeque<Integer> L = new LinkedListDeque<Integer>();
        LinkedListDeque<Integer> L1 = new LinkedListDeque<Integer>(L);

    }

    public void addFirst(T item){
        IntNode<T> items = new IntNode<T>(item);
        if (first == null){
            first = items;
            last = items;
            size++;
            return
        }
        first.prev = items;
        items.next = first;
        first = items;
        size++;
    }

    public void addLast(T item){
        IntNode<T> items = new IntNode<T>(item);
        if (first == null){
            first = items;
            last = items;
            size++;
            return
        }
        last.next = items;
        items.prev = last;
        last = items;
        size++;
    }

    public boolean isEmpty(){
        return first == null;
    }
    // Returns the number of items in the deque.
    public int size(){
        return size;
    }
    // Returns a string showing the items in the deque from first to last,
    // separated by a space.
    public String toString(){
        String a = "";
        IntNode<T> b = first;
    }
    // Removes and returns the item at the front of the deque.
    // If no such item exists, returns null.
    public T removeFirst()
    // Removes and returns the item at the back of the deque.
    // If no such item exists, returns null.
    public T removeLast()
    // Gets the item at the given index, where 0 is the front, 1 is the next item,
    // and so forth. If no such item exists, returns null. Must not alter the deque!
    public T get(int index)
}