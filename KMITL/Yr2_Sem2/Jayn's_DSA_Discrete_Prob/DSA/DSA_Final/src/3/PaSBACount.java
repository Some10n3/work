//    public class PaSBACount {
//    public static long count(SortedBitArray[] packedArrays) {
//        long totalOnes = 0;
//        for (SortedBitArray array : packedArrays) {
//            totalOnes += countOnes(array);
//        }
//        return totalOnes;
//    }
//
//    private static long countOnes(SortedBitArray array) {
//        int length = array.length();
//        int firstOnePosition = findFirstOne(array, 0, length - 1);
//        if (firstOnePosition == -1) {
//            return 0; // No ones found in the array
//        }
//        return length - firstOnePosition;
//    }
//
//    private static int findFirstOne(SortedBitArray array, int start, int end) {
//        int result = -1;
//        while (start <= end) {
//            int mid = start + (end - start) / 2;
//            if (array.get(mid) == 1) {
//                result = mid;
//                end = mid - 1; // Continue searching for the first occurrence on the left
//            } else {
//                start = mid + 1;
//            }
//        }
//        return result;
//    }
//
//    public static void main(String[] args) {
//        // Example packedArrays
//        SortedBitArray[] packedArrays = {
//                new PackedSortedBitArray(5, 2),
//                new PackedSortedBitArray(3, 1),
//                new PackedSortedBitArray(4, 2),
//                new PackedSortedBitArray(7, 3)
//        };
//
//        // Testing
//        System.out.println(count(packedArrays)); // Output: 11
//    }
//}
