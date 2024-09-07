import java.util.Scanner;

public class ParentThread {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        int parentResult = 0;

        for (int i = 1; i <= number; i++) {
            parentResult += i;
        }
        
        ChildThread childThread = new ChildThread(number);
        childThread.start();
        try {
            childThread.join();  // Wait for the child thread to finish
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        int finalResult = parentResult + childThread.getResult();
        System.out.println("Parent result: " + parentResult);
        System.out.println("Child result: " + childThread.getResult());
        System.out.println("Final result: " + finalResult);
    }
}

class ChildThread extends Thread {
    private int number;
    private int result;

    public ChildThread(int number) {
        this.number = number;
    }

    public int getResult() {
        return result;
    }

    @Override
    public void run() {
        result = 0;
        for (int i = 1; i <= 2 * number; i++) {
            result += i;
        }
    }
}

