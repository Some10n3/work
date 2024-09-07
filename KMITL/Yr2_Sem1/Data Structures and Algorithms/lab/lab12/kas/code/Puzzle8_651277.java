package code;

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Stack;

public class Puzzle8_651277 {
    private static final int size = 3;
    private int[] sequence = new int[size * size];
    public List<Puzzle8State> explored = new ArrayList<>(); 
    private Stack<Puzzle8State> stack = new Stack<>();
    

    // Constructor
    public Puzzle8_651277(int[] inputArray) {
        for(int i = 0; i < inputArray.length; i += 3) {
            int tileValue = inputArray[i];
            int row = inputArray[i + 1];
            int col = inputArray[i + 2];
            sequence[row * size + col] = tileValue;
            // System.out.println("tilevalue : " + tileValue);
            // System.out.println("row : " + row);
            // System.out.println("col : " + col);
            // System.out.println("row * size + col : " + (row * size + col));
        }
    }

    public void displayBoard() {
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                int tile = sequence[i * size + j];
                if(tile == 9) { // assuming 9 denotes blank tile
                    System.out.print("  ");
                } else {
                    System.out.print(tile + " ");
                }
            }
            System.out.println();
        }
    }

    private int findBlankPosition() {
        for (int i = 0; i < sequence.length; i++) {
            if (sequence[i] == 9) {
                return i;
            }
        }
        return -1;
    }

    private int findBlankPositionInSequence(int[] sequence) {
        for (int i = 0; i < sequence.length; i++) {
            if (sequence[i] == 9) {
                return i;
            }
        }
        return -1;
    }

    public void generateNextMove() {
        int blankPos = findBlankPosition();

        // Check south
        if (blankPos + 3 < size * size) {
            swapAndPrint(blankPos, blankPos + 3, "south");
        }

        // Check north
        if (blankPos - 3 >= 0) {
            swapAndPrint(blankPos, blankPos - 3, "north");
        }

        // Check east
        if (blankPos % 3 < 2) {
            swapAndPrint(blankPos, blankPos + 1, "east");
        }

        // Check west
        if (blankPos % 3 > 0) {
            swapAndPrint(blankPos, blankPos - 1, "west");
        }
    }

    public List<Puzzle8State> generateNextMove(Puzzle8State currentState) {
        List<Puzzle8State> nextMoves = new ArrayList<>();
        int[] currentSequence = currentState.sequence;
        int blankPos = findBlankPositionInSequence(currentSequence);
    
        // Check south
        if (blankPos + 3 < size * size) {
            nextMoves.add(swapAndReturnNewState(currentSequence, blankPos, blankPos + 3));
        }
    
        // Check north
        if (blankPos - 3 >= 0) {
            nextMoves.add(swapAndReturnNewState(currentSequence, blankPos, blankPos - 3));
        }
    
        // Check east
        if (blankPos % 3 < 2) {
            nextMoves.add(swapAndReturnNewState(currentSequence, blankPos, blankPos + 1));
        }
    
        // Check west
        if (blankPos % 3 > 0) {
            nextMoves.add(swapAndReturnNewState(currentSequence, blankPos, blankPos - 1));
        }
    
        return nextMoves;
    }
    
    private Puzzle8State swapAndReturnNewState(int[] sequence, int blankPos, int targetPos) {
        int[] clonedSequence = sequence.clone();
        int temp = clonedSequence[blankPos];
        clonedSequence[blankPos] = clonedSequence[targetPos];
        clonedSequence[targetPos] = temp;
    
        return new Puzzle8State(clonedSequence);
    }
    
    

    private void swapAndPrint(int blankPos, int targetPos, String direction) {
        int[] clonedSequence = sequence.clone();
        int temp = clonedSequence[blankPos];
        clonedSequence[blankPos] = clonedSequence[targetPos];
        clonedSequence[targetPos] = temp;
    
        Puzzle8State newState = new Puzzle8State(clonedSequence);
    
        if (!explored.contains(newState)) { 
            explored.add(newState);
            System.out.println("Pushing " + direction + " " + Arrays.toString(clonedSequence));
        }
    }

    private int popCount = 0;  

    public void nextMoveWithStack() {
        Puzzle8State initialState = new Puzzle8State(sequence);
        stack.push(initialState);
        
        boolean foundGoal = false;  // Variable to track if the goal is found
        
        while(!stack.isEmpty()) {
            Puzzle8State currentState = stack.pop();
            popCount++;
    
            // Print the status after each pop
            System.out.println("number of pop invocation = " + popCount + 
                               " stack size = " + stack.size() + 
                               " explored size = " + explored.size());
        
            if(isGoal(currentState)) {
                System.out.println("from isGoal [" + Arrays.toString(currentState.sequence) + 
                                   "] found goal [" + Arrays.toString(currentState.sequence) + 
                                   "] let's terminate the loop");
                foundGoal = true;  // Mark the goal as found
                break;  // Terminate the loop
            }
        
            for(Puzzle8State nextState : generateNextMove(currentState)) {
                if(isGoal(nextState)) {  // Check if the next state is the goal
                    System.out.println("from nextState [" + Arrays.toString(nextState.sequence) + 
                                       "] \nfound goal [" + Arrays.toString(nextState.sequence) + 
                                       "] let's terminate the loop");
                    foundGoal = true;  // Mark the goal as found
                    break;  // Terminate the inner loop
                }
                if(!explored.contains(nextState)) {
                    explored.add(nextState);
                    stack.push(nextState);
                }
            }
    
            if(foundGoal) {  // Check if the goal was found in the inner loop and break the main loop
                break;
            }
        }
        
        if (stack.isEmpty() && !foundGoal) {
            System.out.println("Couldn't find a solution");
        }
    }
    

    private boolean isGoal(Puzzle8State state) {
        return Arrays.equals(state.sequence, new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9});
        
    }
    
}
