import java.util.ArrayList;

public class Subsel{
    public static void main(String args[]) {
        int[] a = {1,2,3,4,5,6,7,8,9,10};
        int[] b = takeEvery(a, 3);
        for(int i = 0; i < b.length; i++){
            System.out.println(b[i]);
        }
    }
    // public static int[] takeEvery(int[] a, int stride, int beginWith){
    //     ArrayList<Integer> b = new ArrayList<>();
    // }
    public static int[] takeEvery(int[] a, int stride){
        ArrayList<Integer> b = new ArrayList<>();
        for(int i = 0; i < a.length; i++){
            if(i % stride == 0){
                b.add(a[i]);
            }
        }
        int[] c = new int[b.size()];
        for(int i = 0; i < b.size(); i++){
            c[i] = b.get(i);
        }
        return c;
    }
}