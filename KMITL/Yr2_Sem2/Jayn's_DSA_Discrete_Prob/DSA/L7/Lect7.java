import java.util.function.*;
/*

def add_two(x: int) -> int:
    return x + 2

def twice(f: int => int, x: int) -> int:
    return f(f(x))

twice(add_two, 5) # ==> f(f(5)) ==> add_two(add_two(5)) = 5 + 2 + 2 = 9

 */
// An interface as a makeshift solution to the lack of func. references
//interface IntUnaryFunction {
//    int apply(int x);
//}
//class AddTwo implements IntUnaryFunction {
//    public int apply(int x) { return x + 2; }
//}

interface HasIsLargerThan<T> {
    boolean isLargerThan(T that);
}

class Cat implements HasIsLargerThan<Cat> {
    private int weight;

    Cat(int w) { 
        this.weight = w; 
    }

    public int getWeight() { 
        return this.weight; 
    }

    @Override
    public boolean isLargerThan(Cat that) {
        return this.getWeight() < that.getWeight();
    }

}

public class Lect7 {
    static boolean isLargerByWeight(Cat x, Cat y) {
        return x.getWeight() < y.getWeight();
    }
    public static void main(String[] args) {

        Cat[] items = { new Cat(2), new Cat(7), new Cat(9) };

        int answer = maxIndex(items, Lect7::isLargerByWeight);
        // GOAL: replace an explicit function with an in-place anonymous func
        int answer1 = maxIndex(
                items,
                (Cat x, Cat y) -> x.getWeight() < y.getWeight()
        );

        int answer2 = maxIndex(items); // Why can't items be passed in already?

    }
    //    static int twice(IntUnaryFunction f, int x) {
//        return f.apply(f.apply(x));
//    }
    // Type Bound: For T which implements HasIsLargerThan<T>
    static<T extends HasIsLargerThan<T>> int maxIndex(T[] items) {
        if (items.length == 0)
            return -1;

        int maxDex = 0;
        for (int index=1;index<items.length;index++) {
//            if (items[index] > items[maxDex])
            if (items[index].isLargerThan(items[maxDex]))
                maxDex = index;
        }
        return maxDex;
    }
    
    static<T> int maxIndex(T[] items, BiFunction<T, T, Boolean> isLarger) {
        if (items.length == 0)
            return -1;

        int maxDex = 0;
        for (int index=1;index<items.length;index++) {
//            if (items[index] > items[maxDex])
            if (isLarger.apply(items[index], items[maxDex]))
                maxDex = index;
        }
        return maxDex;
    }
}