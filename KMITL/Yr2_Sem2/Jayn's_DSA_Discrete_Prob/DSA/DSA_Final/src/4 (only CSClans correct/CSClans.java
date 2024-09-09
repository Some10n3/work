import java.util.*;

public class CSClans {
    private Map<String, Integer> cats = new HashMap<>();
    private Map<String, Set<String>> connections = new HashMap<>();
    private Map<String, String> clanLeaders = new HashMap<>();

    public void set(String name, int evilAura) {
        cats.put(name, evilAura);
        if (!connections.containsKey(name)) {
            connections.put(name, new HashSet<>());
        }
        if (!clanLeaders.containsKey(name)) {
            clanLeaders.put(name, name);
        }
    }

    public void tailShake(String catA, String catB) {
        if (!cats.containsKey(catA) || !cats.containsKey(catB)) {
            throw new IllegalArgumentException("Both cats must be in the society.");
        }
        Set<String> catAConnections = connections.get(catA);
        Set<String> catBConnections = connections.get(catB);
        catAConnections.add(catB);
        catBConnections.add(catA);
        String catALeader = findClanLeader(catA);
        String catBLeader = findClanLeader(catB);
        if (!catALeader.equals(catBLeader)) {
            mergeClans(catALeader, catBLeader);
        }
    }

    private String findClanLeader(String cat) {
        String leader = clanLeaders.get(cat);
        if (!leader.equals(cat)) {
            leader = findClanLeader(leader);
            clanLeaders.put(cat, leader);
        }
        return leader;
    }

    private void mergeClans(String leaderA, String leaderB) {
        String newLeader = leaderA.compareTo(leaderB) < 0 ? leaderA : leaderB;
        String oldLeader = leaderA.equals(newLeader) ? leaderB : leaderA;
        clanLeaders.put(oldLeader, newLeader);
    }

    public Map<String, Double> report() {
        Map<String, List<Integer>> clanEvilAuras = new HashMap<>();
        for (String cat : cats.keySet()) {
            String leader = findClanLeader(cat);
            clanEvilAuras.computeIfAbsent(leader, k -> new ArrayList<>()).add(cats.get(cat));
        }
        Map<String, Double> result = new HashMap<>();
        for (Map.Entry<String, List<Integer>> entry : clanEvilAuras.entrySet()) {
            double sum = entry.getValue().stream().mapToInt(Integer::intValue).sum();
            double average = sum / (double) entry.getValue().size();
            result.put(entry.getKey(), average);
        }
        return result;
    }

    public static void main(String[] args) {
        CSClans cs = new CSClans();
        cs.set("Beth", 8);
        cs.set("Deb", 50);
        cs.set("Jolie", 2);
        cs.set("Alice", 23);
        cs.tailShake("Jolie", "Deb");
        cs.set("Jolie", 10);
        cs.set("Vera", 4);
        cs.set("Cathy", 21);
        cs.tailShake("Cathy", "Beth");
        cs.tailShake("Beth", "Vera");
        cs.set("Alice", 21);

        Map<String, Double> report = cs.report();
        System.out.println("Clans and their average evil aura values:");
        for (Map.Entry<String, Double> entry : report.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
