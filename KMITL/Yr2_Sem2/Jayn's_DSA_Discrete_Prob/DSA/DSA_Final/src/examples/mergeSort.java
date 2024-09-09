package examples;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;


// * Check LostItems.java for usecase *


public class mergeSort {
    
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
        Integer[] array = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
        mergeSort(array, Integer::compareTo);
        System.out.println(Arrays.toString(array));
    }
}
