public class Last {
    public static Integer binarySearchLast(int[] a, int k) {
        int low = 0;
        int high = a.length - 1;
        Integer result = null;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (a[mid] == k) {
                result = mid;  // Update the result and continue searching to the right
                low = mid + 1;
            } else if (a[mid] < k) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 2, 2, 4, 5};
        System.out.println(binarySearchLast(arr1, 2));  // Output: 3

        int[] arr2 = {1, 2, 2, 2, 4, 5};
        System.out.println(binarySearchLast(arr2, 0));  // Output: null

        int[] arr3 = {1, 2, 2, 2, 4, 5};
        System.out.println(binarySearchLast(arr3, 5));  // Output: 5
    }
}
