//Lecture 14
import java.util.Arrays;

//Lecture 15
import java.util.Comparator;
import java.util.ArrayList;
import java.util.Random;

//Lecture 17 (Priority Queue)
import java.util.Arrays;
import java.util.Comparator;
import java.util.NoSuchElementException;

public class L14_22 {
    public static void main(String[] args) {
        //Lecture 14 binary search
        String[] array = {"ab", "cc", "bex", "def"};

        System.out.println(Lecture14.linearSearch(array, "cc")); // should return 1
        System.out.println(Lecture14.binarySearch(array, "cc")); // should return 1

        //Lecture 15 insertion sort, quick sort, merge sort
        Integer[] arr = {5, 3, 7, 2, 8, 1, 6, 4};
        Comparator<Integer> comparator = Comparator.naturalOrder();
        
        System.out.println("Before sorting:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Using insertion sort
        Lecture15.insertionSort(arr, comparator);
        System.out.println("After insertion sort:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Using quick sort
        Lecture15.quickSort(arr, comparator);
        System.out.println("After quick sort:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Using merge sort
        Lecture15.mergeSort(arr, comparator);
        System.out.println("After merge sort:");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        //Lecture 17 (priority queue)
        MyPriorityQueue<Integer> pq = new MyPriorityQueue<>(Integer::compareTo);
        pq.enqueue(3);
        pq.enqueue(2);
        pq.enqueue(15);
        pq.enqueue(5);
        pq.enqueue(4);
        pq.enqueue(45);
        System.out.println(pq.findMax());
        System.out.println(pq);
        System.out.println(pq.isEmpty());
        pq.removeMax();
        System.out.println(pq);
        

    }
}

class Lecture14 {
    public static int linearSearch(String[] array, String targetKey) {
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals(targetKey)) {
                return i;
            }
        }
        return -1;
    }

    public static int binarySearch(String[] array, String targetKey) {
        int low = 0;
        int high = array.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            int compare = targetKey.compareTo(array[mid]);
            if (compare == 0) {
                return mid;
            } else if (compare < 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }
    // Determine the running time of the following recursive functions (primSum and whazIt):

    
    public static int primSum(int[] xs) {
        //base case
        if (xs.length == 1) return xs[0];                         //runs O(1)
        if (xs.length == 2) return xs[0] + xs[1];                 //runs O(1)
        else {
            int[] ys = Arrays.copyOfRange(xs, 1, xs.length); //copy of the array from the second element to the end. runs O(n - 1) = O(n)
            return xs[0]+xs[1]+primSum(ys); //recursive call. runs O(n-1) times + O(1) = O(n)
        }
   }                                                               //total running time = O(n) * O(n) = O(n^2)
   
   public static int whazIt(int[] ys) {
       if (ys.length == 0) return 0;            //runs O(1)
       if (ys.length == 1) return ys[0];        //runs O(1)
       int n = ys.length;                       //runs O(1)
       int m = n/2;                             //runs O(1)
       for (int i=0;i<n;i++) {                  //runs O(n)
           int theSum = 0;                                 //runs O(1)
           for (int j=0;j<=i;j++) { theSum += ys[j]; }     //runs O(i)
           ys[i] = theSum;                                 //runs O(1)
       }                                                   //total running time = O(n(n - 1)/2) = O(n^2) / 2 = O(n^2)

       //cuts the array in half and makes two recursive calls
       int a = whazIt(Arrays.copyOfRange(ys, 0, m));     //runs O(n/2) for copying the array + calls O(log(n)) times = O(n/2) * O(log(n)) = O(nlog(n))
       int b = whazIt(Arrays.copyOfRange(ys, m, ys.length));  //runs O(n/2) for copying the array + calls O(log(n)) times = O(n/2) * O(log(n)) = O(nlog(n))
       // the recursive calls are are each O(log(n)) times because the array is cut in half each time

       return a + b;                            //runs O(1)
       //total running time = O(n^2) + O(nlog(n)) + O(nlog(n)) + O(1) = O(n^2) + O(nlog(n)) which is O(n^2) because O(nlog(n)) is less than O(n^2)
       // so the total running time is O(n^2)
   }
}

class Lecture15 {
    public static <T> void insertionSort(T[] array, Comparator<T> cc) {
        int n = array.length;
        for (int i = 1; i < n; ++i) {
            T key = array[i];
            int j = i - 1;

            while (j >= 0 && cc.compare(array[j], key) > 0) {
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = key;
        }
    }

    public static <T> void quickSort(T[] array, Comparator<T> cc) {
        ArrayList<T> arrayList = new ArrayList<>();
        for (T item : array) {
            arrayList.add(item);
        }
        quickSortHelper(arrayList, cc, 0, arrayList.size() - 1);
        for (int i = 0; i < arrayList.size(); i++) {
            array[i] = arrayList.get(i);
        }
    }

    private static <T> void quickSortHelper(ArrayList<T> array, Comparator<T> cc, int low, int high) {
        if (low < high) {
            int pi = partition(array, cc, low, high);
            quickSortHelper(array, cc, low, pi - 1);
            quickSortHelper(array, cc, pi + 1, high);
        }
    }

    private static <T> int partition(ArrayList<T> array, Comparator<T> cc, int low, int high) {
        Random rand = new Random();
        int randomIndex = rand.nextInt(high - low + 1) + low;
        T pivot = array.get(randomIndex);
        swap(array, randomIndex, high);
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (cc.compare(array.get(j), pivot) <= 0) {
                i++;
                swap(array, i, j);
            }
        }
        swap(array, i + 1, high);
        return i + 1;
    }

    private static <T> void swap(ArrayList<T> array, int i, int j) {
        T temp = array.get(i);
        array.set(i, array.get(j));
        array.set(j, temp);
    }

    public static <T> void mergeSort(T[] array, Comparator<T> cc) {
        ArrayList<T> arrayList = new ArrayList<>();
        for (T item : array) {
            arrayList.add(item);
        }
        mergeSortHelper(arrayList, cc, 0, arrayList.size() - 1);
        for (int i = 0; i < arrayList.size(); i++) {
            array[i] = arrayList.get(i);
        }
    }

    private static <T> void mergeSortHelper(ArrayList<T> array, Comparator<T> cc, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;
            mergeSortHelper(array, cc, left, middle);
            mergeSortHelper(array, cc, middle + 1, right);
            merge(array, cc, left, middle, right);
        }
    }

    private static <T> void merge(ArrayList<T> array, Comparator<T> cc, int left, int middle, int right) {
        ArrayList<T> leftArray = new ArrayList<>(array.subList(left, middle + 1));
        ArrayList<T> rightArray = new ArrayList<>(array.subList(middle + 1, right + 1));

        int i = 0, j = 0, k = left;

        while (i < leftArray.size() && j < rightArray.size()) {
            if (cc.compare(leftArray.get(i), rightArray.get(j)) <= 0) {
                array.set(k++, leftArray.get(i++));
            } else {
                array.set(k++, rightArray.get(j++));
            }
        }

        while (i < leftArray.size()) {
            array.set(k++, leftArray.get(i++));
        }

        while (j < rightArray.size()) {
            array.set(k++, rightArray.get(j++));
        }
    }

}


//Lecture 17
class MyPriorityQueue<T> {

    //implement binary heap
    private T[] heap;
    private int size;
    private Comparator<T> cc;

    public MyPriorityQueue(Comparator<T> cc) {
        this(cc, 10);
    }

    public MyPriorityQueue(Comparator<T> cc, int capacity) {
        this.cc = cc;
        heap = (T[]) new Object[capacity];
        size = 0;
    }

    public int left(int i) {
        return 2 * i + 1;
    }

    public int right(int i) {
        return 2 * i + 2;
    }

    public int parent(int i) {
        return (i - 1) / 2;
    }

    public void enqueue(T value) {
        if (size == heap.length) {
            heap = Arrays.copyOf(heap, size * 2);
        }
        heap[size] = value;
        swim(size);
        size++;
    }

    public void dequeue() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        heap[0] = heap[size - 1];
        size--;
        sink(0);
    }

    public void swim(int k) {
        while (k > 0 && cc.compare(heap[parent(k)], heap[k]) < 0) {
            swap(k, parent(k));
            k = parent(k);
        }
    }

    public void sink(int k) {
        while (left(k) < size) {
            int j = left(k);
            if (right(k) < size && cc.compare(heap[right(k)], heap[left(k)]) > 0) {
                j = right(k);
            }
            if (cc.compare(heap[k], heap[j]) > 0) {
                break;
            }
            swap(k, j);
            k = j;
        }
    }

    public void swap(int i, int j) {
        T temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    public T remove() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        T result = heap[0];
        heap[0] = heap[size - 1];
        size--;
        sink(0);
        return result;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public T findMax() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        return heap[0];
    }

    public int size() {
        return size;
    }

    public void removeMax() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        swap(0, size - 1);
        size--;
        sink(0);
    }

    public String toString() {
        return Arrays.toString(Arrays.copyOf(heap, size));
    }

}
