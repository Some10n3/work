package code;

public class MyArray {
    private int maxSize = 100_000;
    private int aSize = 0;
    private int[] a1;

    public MyArray(){
        aSize = 0;
        a1 = new int[maxSize];
    }

    public MyArray(int maxSize){
        if (maxSize <= 0) {
            throw new IllegalArgumentException("maxSize must be >= 0");
        }
        else{
            this.maxSize = maxSize;
            a1 = new int[maxSize];
            aSize = 0;
        }
    }

    public void add(int d){
        if(aSize == maxSize){
            int[] temp = new int[maxSize * 2];
            for(int i = 0; i < maxSize; i++){
                temp[i] = a1[i];
            }
            a1 = temp;
            maxSize *= 2;
        }
        else{
            //System.out.println("aSize: " + aSize);
            //System.out.println("maxSize: " + maxSize);
            //System.out.println("a1.length: " + a1.length);
            a1[aSize] = d;
            aSize++;
        }
      }
      
      public void insert(int d, int index){
        for(int i = aSize; i > index; i--){
            a1[i] = a1[i - 1];
        }
        a1[index] = d;
        aSize++;
      }
    
      public int find(int d){
        for(int i = 0; i < aSize; i++){
          if(a1[i] == d){
            return i;
          }
        }
        return -1;
      }
    
      public int binarySearch(int d){
        int low = 0;
        int high = aSize - 1;
        int mid;
        while(low <= high){
          mid = (low + high) / 2;
          if(a1[mid] == d){
            return mid;
          }
          else if(a1[mid] < d){
            low = mid + 1;
          }
          else{
            high = mid - 1;
          }
        }
        return -1;
      }
    
      public void delete(int index){
        if(aSize != 0){
            for(int i = index; i < aSize - 1; i++){
            a1[i] = a1[i + 1];
            }
            aSize--;
        }
      }
    
      @Override
      public String toString(){
        String s = "";
        for(int i = 0; i < aSize; i++){
          s += a1[i] + " ";
        }
        return s;
      }
    
    
      public boolean equals(MyArray n){
        if(aSize != n.aSize){
          return false;
        }
        else{
          for(int i = 0; i < aSize; i++){
            if(a1[i] != n.a1[i]){
              return false;
            }
          }
          return true;
        }
      }
    

    public boolean isFull(){
        return aSize == maxSize;
    }

    public boolean isEmpty(){
        return aSize == 0;
    }

    public int[] expandByK(int k){
        if (k <= 0) {
            throw new IllegalArgumentException("k must be >= 0");
        }
        else{
            int[] temp = new int[maxSize + k];
            for(int i = 0; i < maxSize; i++){
                temp[i] = a1[i];
            }
            a1 = temp;
            maxSize += k;
            return a1;
        }
    }

    public int[] expand(){
        return expandByK(2);
    }
    

}
