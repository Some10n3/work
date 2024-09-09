import java.util.Comparator;
import java.util.ArrayList;
import java.util.Random;

public class Lecture15 {
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

    public static void main(String[] args) {

        Integer[] arr = {5, 3, 7, 2, 8, 1, 6, 4};
        Comparator<Integer> comparator = Comparator.naturalOrder();

        System.out.println("Before sorting:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Using insertion sort
        insertionSort(arr, comparator);
        System.out.println("After insertion sort:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Using quick sort
        quickSort(arr, comparator);
        System.out.println("After quick sort:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Using merge sort
        mergeSort(arr, comparator);
        System.out.println("After merge sort:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
