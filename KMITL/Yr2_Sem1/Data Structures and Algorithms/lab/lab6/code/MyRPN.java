package code;
import code.MyStackL;
import java.util.regex.Pattern;
import java.util.StringTokenizer;

public class MyRPN {
    private static Pattern pattern = Pattern.compile("-?\\d+(\\.\\d+)?");
    public static boolean isNumeric(String strNum) {
        if (strNum == null) return false;
        return pattern.matcher(strNum).matches();
    }
    public static double computeRPN(String rpn) {
        MyStackL stack = new MyStackL();
        StringTokenizer st = new StringTokenizer(rpn);
        while (st.hasMoreTokens()) {
            String t = st.nextToken();
            if (isNumeric(t)) stack.push(t);
            else {
                double a = Double.parseDouble(stack.pop());
                double b = Double.parseDouble(stack.pop());
                switch (t) {
                    case "+":
                        stack.push(Double.toString(a + b));
                        break;
                    case "-":
                        stack.push(Double.toString(b - a));
                        break;
                    case "*":
                        stack.push(Double.toString(a * b));
                        break;
                    case "/":
                        stack.push(Double.toString(b / a));
                        break;
                    default:
                        break;
                }
            }
        }
        return Double.parseDouble(stack.pop());
    }
}