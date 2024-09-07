
package code;

public class Puzzle8 {
    int size;
    int[][] sequence;

    public Puzzle8(int[] inputArray) {
        this.size = 3;
        this.sequence = new int[size][size];

        // Fill the sequence with values from the input array
        for (int idx = 0; idx < inputArray.length; idx++) {
            int row = idx / size;
            int col = idx % size;
            this.sequence[row][col] = inputArray[idx];
        }
    }

    public void displayBoard() {
        for (int row = 0; row < size; row++) {
            for (int col = 0; col < size; col++) {
                System.out.print(sequence[row][col] + " ");
            }
            System.out.println();
        }
    }
}
