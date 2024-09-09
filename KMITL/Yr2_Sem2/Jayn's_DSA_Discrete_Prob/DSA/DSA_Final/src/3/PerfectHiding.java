import java.util.*;

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

public class PerfectHiding {

    static List<List<WeightedEdge>> graph;

    public static int bestSpotDistance(List<WeightedEdge> passages) {
        // Construct the graph
        constructGraph(passages);

        // Perform DFS from chamber 1 to find the farthest chamber
        int[] distance = new int[graph.size()];
        dfs(1, -1, distance);

        // Find the maximum distance
        int maxDistance = 0;
        for (int dist : distance) {
            maxDistance = Math.max(maxDistance, dist);
        }

        return maxDistance;
    }

    private static void constructGraph(List<WeightedEdge> passages) {
        int n = passages.size() + 1;
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (WeightedEdge edge : passages) {
            graph.get(edge.first).add(edge);
        }
    }

    private static void dfs(int node, int parent, int[] distance) {
        for (WeightedEdge edge : graph.get(node)) {
            int neighbor = edge.second;
            if (neighbor != parent) {
                distance[neighbor] = distance[node] + edge.cost;
                dfs(neighbor, node, distance);
            }
        }
    }

//Manually add edge to list
//    public static void main(String[] args) {
//        // Example graph
//        List<WeightedEdge> passages = new ArrayList<>();
//        passages.add(new WeightedEdge(1, 4, 3));
//        passages.add(new WeightedEdge(4, 2, 8));
//        passages.add(new WeightedEdge(4, 3, 3));
//        passages.add(new WeightedEdge(3, 5, 4));
//        passages.add(new WeightedEdge(1, 6, 9));
//        passages.add(new WeightedEdge(6, 7, 1));
//
//        System.out.println(bestSpotDistance(passages)); // Output: 11
//    }
//}

    public static void main(String[] args) {
        List<WeightedEdge> passages = new ArrayList<>(Arrays.asList(
                WeightedEdge.Edge(1, 2, 1),
                WeightedEdge.Edge(2, 3, 2),
                WeightedEdge.Edge(2, 4, 5)));
        int expcted = 6;
        boolean verdict = bestSpotDistance(passages)==expcted;
        System.out.println("verdict: "+verdict);
    }
}
