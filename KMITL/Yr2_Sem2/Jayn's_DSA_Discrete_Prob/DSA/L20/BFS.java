import java.util.*;

interface UndirectedGraph<Vertex> {
    int numEdges(); // How many edges?
    int numVertices(); // How many vertices?
    int deg(Vertex v); // Return the degree of v

    // Return an iterable of vertices adjacent to v
    Iterable<Vertex> adj(Vertex v);

    // Is there an edge between u and v?
    boolean isEdge(Vertex u, Vertex v);

    // Add a new vertex
    void addVertex(Vertex v);

    // Add an edge between u and v
    void addEdge(Vertex u, Vertex v);

    // Remove an edge
    void removeEdge(Vertex u, Vertex v);
}

class UndirectedAdjMap<Vertex> implements UndirectedGraph<Vertex> {
    private Map<Vertex, Set<Vertex>> adjMap;

    public UndirectedAdjMap() {
        adjMap = new HashMap<>();
    }

    @Override
    public int numEdges() {
        int count = 0;
        for (Set<Vertex> neighbors : adjMap.values()) {
            count += neighbors.size();
        }
        return count / 2; // Each edge is counted twice
    }

    @Override
    public int numVertices() {
        return adjMap.size();
    }

    @Override
    public int deg(Vertex v) {
        return adjMap.containsKey(v) ? adjMap.get(v).size() : 0;
    }

    @Override
    public Iterable<Vertex> adj(Vertex v) {
        return adjMap.getOrDefault(v, Collections.emptySet());
    }

    @Override
    public boolean isEdge(Vertex u, Vertex v) {
        return adjMap.containsKey(u) && adjMap.get(u).contains(v);
    }

    @Override
    public void addVertex(Vertex v) {
        adjMap.putIfAbsent(v, new HashSet<>());
    }

    @Override
    public void addEdge(Vertex u, Vertex v) {
        addVertex(u);
        addVertex(v);
        adjMap.get(u).add(v);
        adjMap.get(v).add(u);
    }

    @Override
    public void removeEdge(Vertex u, Vertex v) {
        if (adjMap.containsKey(u)) {
            adjMap.get(u).remove(v);
        }
        if (adjMap.containsKey(v)) {
            adjMap.get(v).remove(u);
        }
    }
}

public class BFS {
    static void findShortest(UndirectedGraph<Integer> G, Integer a, Integer b) {
        Map<Integer, Integer> parentMap = new HashMap<>();
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();

        queue.offer(a);
        visited.add(a);
        parentMap.put(a, null);

        while (!queue.isEmpty()) {
            Integer current = queue.poll();
            if (current.equals(b)) {
                printPath(parentMap, b);
                return;
            }
            for (Integer neighbor : G.adj(current)) {
                if (!visited.contains(neighbor)) {
                    queue.offer(neighbor);
                    visited.add(neighbor);
                    parentMap.put(neighbor, current);
                }
            }
        }
        System.out.println("No path found between " + a + " and " + b);
    }

    static void printPath(Map<Integer, Integer> parentMap, Integer node) {
        List<Integer> path = new ArrayList<>();
        while (node != null) {
            path.add(node);
            node = parentMap.get(node);
        }
        Collections.reverse(path);
        for (Integer vertex : path) {
            System.out.print(vertex + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        UndirectedGraph<Integer> G = new UndirectedAdjMap<>();
        // G.addEdge(1, 2);
        // G.addEdge(1, 3);
        // G.addEdge(2, 4);
        // G.addEdge(2, 5);
        // G.addEdge(3, 6);
        // G.addEdge(3, 7);
        // G.addEdge(4, 8);
        // G.addEdge(5, 9);

        G.addEdge(1, 3);
        G.addEdge(3, 2);
        G.addEdge(2, 0);
        G.addEdge(0, 3);

        // findShortest(G, 1, 9);
        // findShortest(G, 1, 8);
        // findShortest(G, 1, 10);

        findShortest(G, 2, 1);
    }
}
