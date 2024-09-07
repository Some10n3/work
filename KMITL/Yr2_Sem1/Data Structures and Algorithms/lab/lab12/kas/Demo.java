import code.Puzzle8State;
import code.Puzzle8_651277;

import java.util.Arrays;

public class Demo {
    public static void main(String[] args) {
        // demo1();
        // demo2();
        demo3();
    }

    static void demo1() {
        int[] inputArray = {9,0,0,1,0,1,3,0,2,4,1,0,2,1,1,5,1,2,7,2,0,8,2,1,6,2,2};
        Puzzle8_651277 game = new Puzzle8_651277(inputArray);
        game.displayBoard();
    }

    static void demo2() {
        Puzzle8_651277 game = new Puzzle8_651277(new int [] {9,0,0,1,0,1,3,0,2,4,1,0,2,1,1,5,1,2,7,2,0,8,2,1,6,2,2});
        game.generateNextMove();
        game.displayBoard();
    }

    static void demo3() {
        Puzzle8_651277 game = new Puzzle8_651277(new int[] {9,0,0,1,0,1,3,0,2,4,1,0,2,1,1,5,1,2,7,2,0,8,2,1,6,2,2});
        game.nextMoveWithStack();
        System.out.println(game.explored.size());
        System.out.println("partial explored state");
        for (Puzzle8State s : game.explored) {
            if (s.sequence[0] == 1 && s.sequence[1] == 2 && s.sequence[2] == 3 && s.sequence[3] == 4 ) {
                System.out.println(Arrays.toString(s.sequence));
            }
        }
        System.out.println("note that the program terminates prior to pushing goal state into explored!!");
        game.displayBoard();
    }
}