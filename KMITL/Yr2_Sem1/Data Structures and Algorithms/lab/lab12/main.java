
import code.Puzzle8;

public class main {
    public static void main(String[] args) {
        demo1();
    }

    public static void demo1() {
        int[] inputArray = {9, 0, 0, 1, 0, 1, 3, 0, 2, 4, 1, 0, 2, 1, 1, 5, 1, 2, 7, 2, 0, 8, 2, 1, 6, 2, 2};
        Puzzle8 game = new Puzzle8(inputArray);
        game.displayBoard();
    }
}
