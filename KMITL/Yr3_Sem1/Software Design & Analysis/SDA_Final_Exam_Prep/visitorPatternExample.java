/*
 * Why Is This Useful?
 * Separation of Concerns: You can keep the node classes simple (e.g., VariableNode, AssignmentNode) and focus them on representing data, while each Visitor handles specific operations. This prevents you from cramming too much logic into your node classes, making the code cleaner and easier to maintain.
 * 
 * Extensibility: You can easily add new operations (e.g., add a new visitor for optimization, type checking, or performance analysis) without changing the node classes. This is especially important in complex systems like compilers, where operations on the data structure grow over time.
 * 
 * Flexibility: You can reuse the same object structure for different purposes. In this example, the same AST is used for semantic analysis and code generation just by passing a different visitor.
 * 
 * Summary: When to Use the Visitor Pattern
 * You have a fixed set of classes (like nodes in an AST) that represent your data structure.
 * You want to add new operations frequently (e.g., printing, checking, transforming, etc.) without modifying the object classes.
 * You want to separate different types of logic (e.g., semantic checking, code generation, optimization) and keep the object structure clean and focused.
 * In cases like compilers, UI frameworks, or even tools that handle file systems or document structures, the Visitor Pattern can simplify operations across complex, hierarchical data structures.
 */



// Visitor Interface
interface Visitor {
    void visit(Book book);
    void visit(Fruit fruit);
}

// Element Interface
interface ItemElement {
    void accept(Visitor visitor);
}

// Concrete Element: Book
class Book implements ItemElement {
    private int price;
    private String isbn;

    public Book(int price, String isbn) {
        this.price = price;
        this.isbn = isbn;
    }

    public int getPrice() {
        return price;
    }

    public String getIsbn() {
        return isbn;
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}

// Concrete Element: Fruit
class Fruit implements ItemElement {
    private int pricePerKg;
    private int weight;
    private String name;

    public Fruit(int pricePerKg, int weight, String name) {
        this.pricePerKg = pricePerKg;
        this.weight = weight;
        this.name = name;
    }

    public int getPricePerKg() {
        return pricePerKg;
    }

    public int getWeight() {
        return weight;
    }

    public String getName() {
        return name;
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}

// Concrete Visitor: Price Calculator
class ShoppingCartVisitor implements Visitor {
    @Override
    public void visit(Book book) {
        System.out.println("Book ISBN: " + book.getIsbn() + " costs: " + book.getPrice());
    }

    @Override
    public void visit(Fruit fruit) {
        System.out.println(fruit.getName() + " costs: " + (fruit.getPricePerKg() * fruit.getWeight()) + " per kg.");
    }
}

public class visitorPatternExample {
    public static void main(String[] args) {
        ItemElement[] items = new ItemElement[] {
            new Book(20, "1234"),
            new Fruit(10, 2, "Apple"),
            new Fruit(5, 5, "Banana")
        };

        Visitor visitor = new ShoppingCartVisitor();

        for (ItemElement item : items) {
            item.accept(visitor);
        }
    }
}
