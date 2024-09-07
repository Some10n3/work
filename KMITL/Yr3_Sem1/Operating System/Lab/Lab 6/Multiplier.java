class Multiplier extends Thread {
    private int[][] multiplicandMatrix;
    private int[][] multiplierMatrix;
    private int row;
    private int column;
    private int result;

    public Multiplier(int[][] multiplicandMatrix, int[][] multiplierMatrix, int row, int column) {
        this.multiplicandMatrix = multiplicandMatrix;
        this.multiplierMatrix = multiplierMatrix;
        this.row = row;
        this.column = column;
    }

    public void run() {
        result = 0;
        for (int i = 0; i < multiplicandMatrix[row].length; i++) {
            result += multiplicandMatrix[row][i] * multiplierMatrix[i][column];
        }
    }

    public int getResult() {
        return result;
    }
}