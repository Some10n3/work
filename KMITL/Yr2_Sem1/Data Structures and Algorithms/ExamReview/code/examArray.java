package code;

public class examArray {
    int maxSize = 100;
    double[] arr = new double[maxSize];
    int currentSize = 0;

    public examArray() {
        currentSize = 0;
    }

    public examArray(int maxSize) {
        if (maxSize <= 0) {
            throw new IllegalArgumentException("maxSize must be >= 0");
        } else {
            this.maxSize = maxSize;
            arr = new double[maxSize];
            currentSize = 0;
        }
    }

    public void add(double d) {
        if (currentSize == maxSize){
            double[] tempArr = new double[maxSize * 2];
            for(int i = 0; i < maxSize; i++){
                tempArr[i] = arr[i];
            }
            tempArr[maxSize] = d;
            arr = tempArr;
            maxSize = 2 * maxSize;
        }
        else{
            arr[currentSize] = d;
            currentSize++;
        }
    }

    public void insert(double d, int index) {
        for(int i = currentSize; i > index; i--){
            arr[i] = arr[i - 1];
        }
        arr[index] = d;
        currentSize++;        
    }

    public int find(double d) {
        for(int i = 0; i < currentSize; i++){
            if(arr[i] == d){
                return i;
            }
        }
    }

    public int binarySearch(double d) {
        int low = 0;
        int high = currentSize - 1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] == d){
                return mid;
            }
            else if(arr[mid] < d){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return -1;
    }

    public void remove(double d) {
        int index = find(d);
        if(index == -1){
            return;
        }
        else{
            for(int i = index; i < currentSize - 1; i++){
                arr[i] = arr[i + 1];
            }
            currentSize--;
        }
    }

    public boolean equals(examArray n) {
        if(currentSize != n.currentSize){
            return false;
        }
        else{
            for(int i = 0; i < currentSize; i++){
                if(arr[i] != n.arr[i]){
                    return false;
                }
            }
            return true;
        }
    }

    public boolean isFull() {
        return currentSize == maxSize;
    }

    public boolean isEmpty() {
        return currentSize == 0;
    }

    public void expandByK(int k) {
        double[] tempArr = new double[maxSize + k];
        for(int i = 0; i < currentSize; i++){
            tempArr[i] = arr[i];
        }
        arr = tempArr;
        maxSize = maxSize + k;
    }

    public String toString() {
        String s = "";
        for(int i = 0; i < currentSize; i++){
            s += arr[i] + " ";
        }
        return s;
    }
}
