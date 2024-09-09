import java.math.BigInteger;

public class Fib {
    public static void main(String[] args) {
        System.out.println(fib(0));
        System.out.println(fib(1));
        System.out.println(fib(2));
        System.out.println(fib(3));
        System.out.println(fib(100));
    }

    public static BigInteger fib(int n) {
        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        BigInteger c = BigInteger.ZERO;
        for (int i = 0; i < n; i++) {
            c = a.add(b);
            a = b;
            b = c;
        }
        return a;
    }
}
