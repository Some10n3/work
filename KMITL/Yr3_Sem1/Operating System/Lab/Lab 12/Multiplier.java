public class Multiplier extends Thread {
    private int[][] a;
    private int[][] b;
    private int row, col;
    private int result;

    public Multiplier(int[][] a, int[][] b, int row, int col) {
        this.a = a;
        this.b = b;
        this.row = row;
        this.col = col;
    }

    @Override
    public void run() {
        // Calculate the dot product of the specified row in "a" and the specified column in "b"
        result = 0;
        for (int i = 0; i < a[0].length; i++) {
            result += a[row][i] * b[i][col];
        }
    }

    public int getResult() {
        return result;
    }
}
