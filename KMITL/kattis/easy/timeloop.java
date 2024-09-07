import java.util.Scanner;
class timeloop{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for (int i = 1; i <= n; i++){
            String outt = "";
            outt += i + " Abracadabra";
            System.out.println(outt);
        }
    }
}