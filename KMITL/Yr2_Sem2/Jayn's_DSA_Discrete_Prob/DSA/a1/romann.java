public class romann {
    public static void main(String args[]) {
        System.out.print(romanToInt("MCMLIV"));
    }

    public static int romanToInt(String romanNum) {
        //I = 1, V = 5, X = 10, L = 50,
        //C = 100, D = 500, M = 1000
        int sum = 0;
        int prev = 0;
        for (char a : romanNum.toCharArray()) {
            int curr = 0;
            System.out.println(a);
            switch (a) {
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
            }
            else {
                sum += curr;
            }
            prev = curr;

            }
        return sum;
        }
    }