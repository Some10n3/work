
// Proxy Pattern : surrogate or placeholder for another object to control access to it.

// Subject
interface Image {
    void display();
}

// RealSubject
class RealImage implements Image {
    private String fileName;

    public RealImage(String fileName) {
        this.fileName = fileName;
        loadImageFromDisk();
    }

    private void loadImageFromDisk() {
        System.out.println("Loading " + fileName);
    }

    @Override
    public void display() {
        System.out.println("Displaying " + fileName);
    }
}

// Proxy
class ProxyImage implements Image {
    private RealImage realImage;
    private String fileName;

    public ProxyImage(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public void display() {
        if (realImage == null) {
            realImage = new RealImage(fileName);
        }
        realImage.display();
    }
}

public class proxyPatternExample {
    public static void main(String[] args) {
        Image image = new ProxyImage("image.jpg");

        // Image will be loaded from disk
        image.display();
        System.out.println("");

        // Image will not be loaded from disk
        image.display();
    }
}
