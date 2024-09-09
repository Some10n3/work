import java.util.Arrays;

public class Lecture14 {
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

    public static void main(String[] args) {
        String[] array = {"ab", "cc", "bex", "def"};

        System.out.println(linearSearch(array, "cc")); // should return 1
        System.out.println(binarySearch(array, "cc")); // should return 1
    }
}