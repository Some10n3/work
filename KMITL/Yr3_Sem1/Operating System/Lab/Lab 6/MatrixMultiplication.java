

public class MatrixMultiplication {
    public static void main(String[] args) {
        int[][] multiplicandMatrix = {
            {5, 6, 7},
            {4, 8, 9}
        };

        int[][] multiplierMatrix = {
            {6, 4},
            {5, 7},
            {1, 1}
        };

        int rows = multiplicandMatrix.length;
        int cols = multiplierMatrix[0].length;

        Multiplier[][] threads = new Multiplier[rows][cols];
        int[][] resultMatrix = new int[rows][cols];

        // Create and start threads
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                threads[i][j] = new Multiplier(multiplicandMatrix, multiplierMatrix, i, j);
                threads[i][j].start();
            }
        }

        // Wait for all threads to finish
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                try {
                    threads[i][j].join();
                    resultMatrix[i][j] = threads[i][j].getResult();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        // Print the result matrix
        System.out.println("Result matrix:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(resultMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
