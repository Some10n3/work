
public class NearFib {

    // helper method for finding the surrounding fibonacci numbers given a number that may or may not be a Fibonacci
    // number. It returns a long array where array[0] is the closest fibonacci number below l (unless l itself is a
    // Fibonacci number, then array[0] is l) and array[1] is
    // the closest fibonacci number greater than l.
    private static long[] surroundingFibs(long l){
        long n1 = 1;
        long n2 = 1;

        long nx = n1 + n2;

        long[] bounds = new long[2];

        long upperBound = 0;
        long lowerBound = 0;
        while (nx <= l){
            n1 = n2;
            n2 = nx;
            nx = n1 + n2;
            if (nx >= l){
                upperBound = nx;
                lowerBound = n2;
            }
        }
        bounds[0] = lowerBound;
        bounds[1] = upperBound;
        return bounds;
    }
    public int numNearFib(long[] a, long t) {
        int counter = 0;
        for (long L: a){
            long lower_diff = Math.abs(surroundingFibs(L)[0] - L);
            long upper_diff = Math.abs(surroundingFibs(L)[1] - L);
            if (Math.min(lower_diff, upper_diff) <= t){
                counter++;
            }
        }
        return counter;
    }
}
