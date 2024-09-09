package a2;
public class MinMax {
    public static double minMaxAverage(int[] numbers) {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalArgumentException("Input array is empty or null");
        }

        int n = numbers.length;

        if (n % 2 == 1) {
            // If the array has an odd length, initialize min and max with the first element
            int myMin = numbers[0];
            int myMax = numbers[0];
            for (int i = 1; i < n - 1; i += 2) {
                // Pairwise comparison
                int smaller = numbers[i] < numbers[i + 1] ? numbers[i] : numbers[i + 1];
                int larger = numbers[i] > numbers[i + 1] ? numbers[i] : numbers[i + 1];

                // Update min and max based on pairwise comparison
                myMin = Math.min(myMin, smaller);
                myMax = Math.max(myMax, larger);
            }

            // Compare the last element with min and max
            myMin = Math.min(myMin, numbers[n - 1]);
            myMax = Math.max(myMax, numbers[n - 1]);

            return (myMin + myMax) / 2.0;
        } else {
            // If the array has an even length, initialize min and max with the first two elements
            int myMin = Math.min(numbers[0], numbers[1]);
            int myMax = Math.max(numbers[0], numbers[1]);

            for (int i = 2; i < n - 1; i += 2) {
                // Pairwise comparison
                if (numbers[i] < numbers[i + 1]) {
                    smaller = numbers[i];
                    larger = numbers[i + 1];
                } else {
                    smaller = numbers[i + 1];
                    larger = numbers[i];
                }

                // Update min and max based on pairwise comparison
                myMin = Math.min(myMin, smaller);
                myMax = Math.max(myMax, larger);
            }

            return (myMin + myMax) / 2.0;
        }
    }

    public static void main(String[] args) {
        int[] numbers = {3, 8, 2, 5, 1, 7, 4, 6};
        double result = minMaxAverage(numbers);
        System.out.println("Average of min and max: " + result);
    }
}
