import java.util.Scanner;

public class WhichIsGreater {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        System.out.print(a > b ? 1 : 0);

        scanner.close();
    }
}