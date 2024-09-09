import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class LostItems {
    public static void main(String[] args) {
        // int[] a = {1, 2, 3, 4, 5};
        // int[] b = {2, 3, 4, 5, 6};
        int[] a = {203, 204, 205, 206, 207, 208, 203, 204, 205, 206} ;
        int[] b = {203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204};
        int[] c = lostItems(a, b);
        System.out.println("Lost items:");
        for (int i = 0; i < c.length; i++) {
            System.out.print(c[i] + " ");
        }
    }

    public static int[] lostItems(int[] a, int b[]){
        Map<Integer, Integer> occurrencesA = countOccurrences(a);
        Map<Integer, Integer> occurrencesB = countOccurrences(b);
        
        HashSet<Integer> lostItems = new HashSet<>();
        
        for (Map.Entry<Integer, Integer> entry : occurrencesA.entrySet()) {
            int num = entry.getKey();
            int countA = entry.getValue();
            int countB = occurrencesB.getOrDefault(num, 0);
            
            if (countA != countB) {
                lostItems.add(num);
            }
        }

        for (Map.Entry<Integer, Integer> entry : occurrencesB.entrySet()) {
            int num = entry.getKey();
            int countB = entry.getValue();
            int countA = occurrencesA.getOrDefault(num, 0);
            
            if (countA != countB) {
                lostItems.add(num);
            }
        }
        
        Integer[] lostItemsArray = lostItems.toArray(new Integer[0]);

        mergeSort(lostItemsArray, Comparator.naturalOrder());

        int[] lostItemsArr = new int[lostItemsArray.length];

        for (int i = 0; i < lostItemsArray.length; i++) {
            lostItemsArr[i] = lostItemsArray[i];
        }

        return lostItemsArr;
    }

    public static Map<Integer, Integer> countOccurrences(int[] array) {
        Map<Integer, Integer> occurrences = new HashMap<>();
        
        for (int num : array) {
            occurrences.put(num, occurrences.getOrDefault(num, 0) + 1);
        }
        
        return occurrences;
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