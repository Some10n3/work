package examples;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Stack;
import java.util.HashMap;

class WeightedEdge {
    int first, second, cost;

    public WeightedEdge(int first, int second, int cost) {
        this.first = first;
        this.second = second;
        this.cost = cost;
    }

    public static WeightedEdge Edge(int first, int second, int cost) {
        return new WeightedEdge(first, second, cost);
    }
}


//traversing a graph from a start node to all other nodes
public class DFS {
    public static void main(String[] args) {
        HashMap<Integer, List<WeightedEdge>> passages = new HashMap<>();
        passages.put(1, Arrays.asList(WeightedEdge.Edge(1, 6, 9), WeightedEdge.Edge(1, 4, 3)));
        passages.put(2, new ArrayList<>());
        passages.put(3, Arrays.asList(WeightedEdge.Edge(3, 5, 4)));
        passages.put(4, Arrays.asList(WeightedEdge.Edge(4, 2, 8), WeightedEdge.Edge(4, 3, 3)));
        passages.put(5, new ArrayList<>());
        passages.put(6, Arrays.asList(WeightedEdge.Edge(6, 7, 1)));
        passages.put(7, new ArrayList<>());
        
        int[] distance = DFS(passages, 1, 7);
        System.out.println("Distances:");
        for (int i = 1; i < distance.length; i++) {
            System.out.println("Node " + i + ": " + distance[i]);
        }
    }

    //Finding shortest distance from node start to all other nodes
    //where passages is a map of nodes and their edges
    //nodeNumber is the number of nodes in the graph
    //start is the node to start from
    public static int[] DFS(HashMap<Integer, List<WeightedEdge>> passages, int start, int nodeNumber) {
        // visited array to keep track of visited nodes
        boolean[] visited = new boolean[nodeNumber + 1];
        // distance array to keep track of shortest distance from start to all other nodes
        int[] distance = new int[nodeNumber + 1];
        // stack to keep track of nodes to visit
        Stack<Integer> stack = new Stack<>();
        
        visited[start] = true;
        stack.push(start);

        while (!stack.isEmpty()) {
            int node = stack.pop();
            
            // iterate through all the edges of the current node
            for (WeightedEdge edge : passages.get(node)) {
                // if the distance from the current node to the next node is less than the current distance
                if (distance[node] + edge.cost < distance[edge.second] || distance[edge.second] == 0)
                    distance[edge.second] = distance[node] + edge.cost;
                // if the next node has not been visited, add it to the stack and mark it as visited
                if (edge.first == node && !visited[edge.second]) {
                    visited[edge.second] = true;
                    distance[edge.second] = distance[node] + edge.cost;
                    stack.push(edge.second);
                }
            }
        }
     
        return distance;
    }
}
