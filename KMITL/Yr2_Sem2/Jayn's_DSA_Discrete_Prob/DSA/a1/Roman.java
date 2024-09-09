public class Roman {
    public static void main(String[] args) {
        romanToInt("III");
        romanToInt("IV");
        romanToInt("IX");
        romanToInt("LVIII");
        romanToInt("MCMLIV");
    }
    public static void romanToInt(String s) {
        int sum = 0;
        int prev = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            System.out.println(s.charAt(i));
            int curr = 0;
            char c = s.charAt(i);
            switch (s.charAt(i)) {
                case 'I':
                    curr = 1;
                    break;
                case 'V':
                    curr = 5;
                    break;
                case 'X':
                    curr = 10;
                    break;
                case 'L':
                    curr = 50;
                    break;
                case 'C':
                    curr = 100;
                    break;
                case 'D':
                    curr = 500;
                    break;
                case 'M':
                    curr = 1000;
                    break;
            }
            if (curr < prev) {
                sum -= curr;
            } else {
                sum += curr;
            }
            prev = curr;
        }
        System.out.println(sum);
    }
}
