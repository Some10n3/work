package code;

public class MyArrDemo<T> {
    public final int MAX_SIZE = 9;
    private int size = 0;
    private Object [] arr = new Object[MAX_SIZE];
    
    public MyArrDemo() {}

    public void add(T instance) {
        arr[size++] = instance;
    }

    public void set(int i, T instance) {
        arr[i] = instance;
    }

    public T get(int i) {
        @SuppressWarnings("unchecked")
        final T element = (T)arr[i];
        return element;
    }
    
    public void swap(int i, int j) {
        T temp = get(i);
        set(i, get(j));
        set(j, temp);
    }
    
    public int currentSize() {
        return size;
    }

    public void selectionSort(MyArrDemo<SillyLuckyNumber> arr){
        for (int i = 0; i < arr.currentSize(); i++) {
            int min = i;
            for (int j = i+1; j < arr.currentSize(); j++) {
                if (arr.get(j).getLuckyNumer() < arr.get(min).getLuckyNumer()) {
                    min = j;
                }
            }
            arr.swap(i, min);
        }
    }

    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer();
        // sb.append("My snapshot looks like this -> ");
        for (int i = 0; i < size; i++)
            sb.append(arr[i] + ",");    
        return sb.toString();
    }
}