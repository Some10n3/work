import java.util.*;

public class XNumber {
    private Map<Integer, Set<Integer>> graph;

    public XNumber(int[][] roster) {
        graph = new HashMap<>();
        buildGraph(roster);
    }

    private void buildGraph(int[][] roster) {
        for (int[] entry : roster) {
            int studentID = entry[0];
            int courseID = entry[1];
            if (!graph.containsKey(studentID)) {
                graph.put(studentID, new HashSet<>());
            }
            graph.get(studentID).add(courseID);
        }
    }

    public int getXnumber(int s, int d) {
        if (!graph.containsKey(s) || !graph.containsKey(d)) {
            return -1; // If either student is not present in the graph, return -1
        }

        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        Map<Integer, Integer> distance = new HashMap<>();

        queue.offer(s);
        visited.add(s);
        distance.put(s, 0);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            if (current == d) {
                return distance.get(current);
            }
            if (graph.containsKey(current)) {
                for (int neighbor : graph.get(current)) {
                    if (!visited.contains(neighbor)) {
                        queue.offer(neighbor);
                        visited.add(neighbor);
                        distance.put(neighbor, distance.get(current) + 1);
                    }
                }
            }
        }
        return -1; // If d is unreachable from s, return -1
    }

    public Set<Integer> getStdByCourse(int courseID) {
        Set<Integer> students = new HashSet<>();
        for (Map.Entry<Integer, Set<Integer>> entry : graph.entrySet()) {
            if (entry.getValue().contains(courseID)) {
                students.add(entry.getKey());
            }
        }
        return students;
    }

    public static void main(String[] args) {
        int[][] roster = {{1,2},{1,3},{1,5},{2,5},{2,4},{3,2},{3,3},{3,1},{4,1},{4,4},{4,6},{5,6},{5,7},{6,9}};
        XNumber xNumber = new XNumber(roster);
        
        System.out.println("XNumber of student 2 considering student 1 as a reference: " + xNumber.getXnumber(1, 2));
        System.out.println("XNumber of student 3 considering student 1 as a reference: " + xNumber.getXnumber(1, 3));
        System.out.println("XNumber of student 4 considering student 1 as a reference: " + xNumber.getXnumber(1, 4));
        System.out.println("XNumber of student 5 considering student 1 as a reference: " + xNumber.getXnumber(1, 5));
        System.out.println("XNumber of student 4 considering student 5 as a reference: " + xNumber.getXnumber(5, 4));
        System.out.println("XNumber of student 5 considering student 4 as a reference: " + xNumber.getXnumber(4, 5));
        
        System.out.println("Students registered for course 2: " + xNumber.getStdByCourse(2));
    }
}
