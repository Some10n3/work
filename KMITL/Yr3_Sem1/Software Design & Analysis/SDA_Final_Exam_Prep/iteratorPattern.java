import java.util.Iterator;
import java.util.ArrayList;
import java.util.List;

// Custom Collection that implements Iterable
class NameCollection implements Iterable<String> {
    private List<String> names = new ArrayList<>();

    public void addName(String name) {
        names.add(name);
    }

    @Override
    public Iterator<String> iterator() {
        return names.iterator();
    }
}

public class iteratorPattern {
    public static void main(String[] args) {
        NameCollection collection = new NameCollection();
        collection.addName("Alice");
        collection.addName("Bob");
        collection.addName("Charlie");

        // Using the Iterator to access elements
        for (String name : collection) {
            System.out.println(name);
        }
    }
}
