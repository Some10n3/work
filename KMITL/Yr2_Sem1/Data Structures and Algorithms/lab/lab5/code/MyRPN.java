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
            if (isNumeric(t)) {
                stack.push(Double.parseDouble(t));
            } else {
                double op2 = stack.pop();
                double op1 = stack.pop();
                switch (t) {
                    case "+":
                        stack.push(op1 + op2);
                        break;
                    case "-":
                        stack.push(op1 - op2);
                        break;
                    case "*":
                        stack.push(op1 * op2);
                        break;
                    case "/":
                        stack.push(op1 / op2);
                        break;
                    default:
                        System.out.println("Invalid operator: " + t);
                        break;
                }
            }
        }
        return stack.pop();
    }
}