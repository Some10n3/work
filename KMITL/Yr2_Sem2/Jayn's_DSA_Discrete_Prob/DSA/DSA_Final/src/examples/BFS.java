package examples;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Queue;
import java.util.HashMap;
import java.util.LinkedList;

public class BFS {
    public static void main(String[] args) {
        HashMap<Integer, List<WeightedEdge>> passages = new HashMap<>();
        passages.put(1, Arrays.asList(WeightedEdge.Edge(1, 6, 9), WeightedEdge.Edge(1, 4, 3)));
        passages.put(2, new ArrayList<>());
        passages.put(3, Arrays.asList(WeightedEdge.Edge(3, 5, 4)));
        passages.put(4, Arrays.asList(WeightedEdge.Edge(4, 2, 8), WeightedEdge.Edge(4, 3, 3)));
        passages.put(5, new ArrayList<>());
        passages.put(6, Arrays.asList(WeightedEdge.Edge(6, 7, 1)));
        passages.put(7, new ArrayList<>());
        
        int[] distance = BFS(passages, 1, 7);
        System.out.println("Distances:");
        for (int i = 1; i < distance.length; i++) {
            System.out.println("Node " + i + ": " + distance[i]);
        }
    }

    //Finding shortest distance from node start to all other nodes
    //where passages is a map of nodes and their edges
    //nodeNumber is the number of nodes in the graph
    //start is the node to start from
    public static int[] BFS(HashMap<Integer, List<WeightedEdge>> passages, int start, int nodeNumber) {
        // visited array to keep track of visited nodes
        boolean[] visited = new boolean[nodeNumber + 1];
        // distance array to keep track of shortest distance from start to all other nodes
        int[] distance = new int[nodeNumber + 1];
        // queue to keep track of nodes to visit
        Queue<Integer> queue = new LinkedList<>();
        
        visited[start] = true;
        queue.add(start);

        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            // iterate through all the edges of the current node
            for (WeightedEdge edge : passages.get(node)) {
                int nextNode = edge.second;
                int cost = edge.cost;
                
                if (!visited[nextNode]) {
                    visited[nextNode] = true;
                    queue.add(nextNode);
                    distance[nextNode] = distance[node] + cost;
                }
            }
        }
        
        return distance;    
    }
}
