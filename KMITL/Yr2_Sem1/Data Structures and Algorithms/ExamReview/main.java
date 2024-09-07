import code.examLinkedList;

public class main {
    public static void main(String[] args) {
        examLinkedList list = new examLinkedList();
        list.add(5);
        list.add(1);
        list.add(4);
        list.add(3);
        // System.out.println(list);   
        // list.setAt(0, 3);
        // System.out.println(list);   
        // list.noUnderstand();
        list.q1Remake(2);
        System.out.println(list);
    }
}
