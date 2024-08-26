// Client code to test the Singleton Logger
public class Singleton {
    public static void main(String[] args) {
        // Get the single instance of Logger
        Logger logger1 = Logger.getInstance();
        Logger logger2 = Logger.getInstance();

        // Test logging
        logger1.log("This is a log message.");

        // Check if both references point to the same instance
        if (logger1 == logger2) {
            System.out.println("logger1 and logger2 are the same instance.");
        } else {
            System.out.println("logger1 and logger2 are different instances.");
        }
    }
}

public class Logger {
    // The sole instance of the class
    private static Logger instance;

    // Private constructor to prevent instantiation
    private Logger() {}

    // Static method to get the single instance of the class
    public static synchronized Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }

    // Method to log messages
    public void log(String message) {
        System.out.println("Log: " + message);
    }
}
