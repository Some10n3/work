public class Zombies {
    public static int countBad(int[] hs) {
        return countBadPairs(hs, 0, hs.length - 1);
    }

    private static int countBadPairs(int[] hs, int left, int right) {
        if (left >= right) {
            return 0;
        }

        int mid = left + (right - left) / 2;

        int count = countBadPairs(hs, left, mid) + countBadPairs(hs, mid + 1, right);
        count += mergeAndCount(hs, left, mid, right);

        return count;
    }

    private static int mergeAndCount(int[] hs, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];
        int count = 0;
        int i = left;
        int j = mid + 1;
        int k = 0;

        while (i <= mid && j <= right) {
            if (hs[i] < hs[j]) {
                count += (mid - i + 1);
                temp[k++] = hs[j++];
            } else {
                temp[k++] = hs[i++];
            }
        }

        while (i <= mid) {
            temp[k++] = hs[i++];
        }

        while (j <= right) {
            temp[k++] = hs[j++];
        }

        for (i = 0; i < temp.length; i++) {
            hs[left + i] = temp[i];
        }

        return count;
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(countBad(new int[]{35, 22, 10}));  // Output: 0
        System.out.println(countBad(new int[]{3, 1, 4, 2}));   // Output: 3
        System.out.println(countBad(new int[]{5, 4, 11, 7}));   // Output: 4
        System.out.println(countBad(new int[]{1, 7, 22, 13, 25, 4, 10, 34, 16, 28, 19, 31}));  // Output: 49
    }
}
