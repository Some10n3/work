public class Main {
    public static void main(String[] args) {
        int[][] array1 = {{5, 6, 7}, {4, 8, 9}};
        int[][] array2 = {{6, 4}, {5, 7}, {1, 1}};
        int rowResult = array1.length;
        int colResult = array2[0].length;
        int[][] result = new int[rowResult][colResult];

        // Define a 2D array of Multiplier threads
        Multiplier[][] threads = new Multiplier[rowResult][colResult];

        // Create and start each thread
        for (int i = 0; i < rowResult; i++) {
            for (int j = 0; j < colResult; j++) {
                threads[i][j] = new Multiplier(array1, array2, i, j);
                threads[i][j].start();
            }
        }

        // Wait for all threads to complete
        for (int i = 0; i < rowResult; i++) {
            for (int j = 0; j < colResult; j++) {
                try {
                    threads[i][j].join();  // Wait for the thread to finish
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        // Store the result from each thread into the result array
        for (int i = 0; i < rowResult; i++) {
            for (int j = 0; j < colResult; j++) {
                result[i][j] = threads[i][j].getResult();
            }
        }

        // Print matrices and result
        System.out.println("First Matrix");
        displayMatrix(array1);
        System.out.println("Second Matrix");
        displayMatrix(array2);
        System.out.println("Result Matrix");
        displayMatrix(result);
    }

    public static void displayMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
    }
}
