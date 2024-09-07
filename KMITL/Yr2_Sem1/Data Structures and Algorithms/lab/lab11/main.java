
import java.util.ArrayList;

public class main {
    public static void main(String[] args) {
        q2();
    }

    static int inf = Integer.MAX_VALUE;

    static void q2() {
        int[][] thisGraph = { { 0,  3,  0,  0,  2 },  // A
                              { 3,  0,  1,  0,  0 },  // B
                              { 0,  1,  0,  4,  0 },  // C
                              { 0,  0,  4,  0,  5 },  // D
                              { 2,  0,  0,  5,  0 }   // E
        };
        System.out.println("computing dfs");
        q2_dfs(thisGraph);
    }
    private static void q2_dfs(int[][] thisGraph) { 
        ArrayList<Integer> stack = new ArrayList<>(); 
        ArrayList<Integer> visited = new ArrayList<>(); 
        stack.add(0); // Start from vertex A (index 0)

        while (!stack.isEmpty()) {
            int parent = stack.get(stack.size() - 1); // Get the top element from the stack
            stack.remove(stack.size() - 1); // Remove it from the stack
            visited.add(parent);

            for (int x = 0; x < thisGraph.length; x++) {
                // System.out.println("Checking edge : " + parent + " -> " + x);
                // System.out.println("Value : " + thisGraph[parent][x]);
                if (thisGraph[parent][x] != 0 && thisGraph[parent][x] != inf && !visited.contains(x)) {
                    stack.add(x); // Add unvisited neighbors to the stack
                    System.out.println("Edge " + parent + " -> " + x);
                }
            }
        }
    }
    private static boolean notEmpty(ArrayList<Integer> stack) { 
        return !stack.isEmpty();
    }
}