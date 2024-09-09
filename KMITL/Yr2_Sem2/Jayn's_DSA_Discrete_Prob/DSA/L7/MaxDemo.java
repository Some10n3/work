import java.util.function.*;

interface HasIsLarger<T>{
    boolean isLarger(T that);
}

class Cat implements HasIsLarger<Cat> {
    private int weight;
    
    Cat(int w) { 
        this.weight = w; 
    }
    
    public int getWeight() { 
        return this.weight; 
    }

    public boolean isLarger(Cat that) {
        return this.getWeight() > that.getWeight();
    }
}


public class MaxDemo {
    static boolean isLargerByWeight(Cat x, Cat y) {
        return x.getWeight() > y.getWeight();
    }

    static<T> T maxIndex(T[] items, BiFunction<T, T, Boolean> isLargerThan){
        if (items.length == 0)
            return null;

        T max = items[0];
        for (int i = 1; i < items.length; i++){
            if (isLargerThan.apply(items[i], max))
                max = items[i];
        }
        return max;
    }


    static<T extends HasIsLarger<T>> T maxIndex(T[] items) {
        if (items.length == 0)
            return null;

        T max = items[0];
        for (int i = 1; i < items.length; i++) {
            if (items[i].isLarger(max))
                max = items[i];
        }
        return max;
    }

    public static void main(String[] args) {
        Cat[] items = { new Cat(3), new Cat(6), new Cat(9) };
        Cat a0 = maxIndex(items, MaxDemo::isLargerByWeight);

        Cat a1 = maxIndex(
                items,
                (Cat x, Cat y) -> x.getWeight() > y.getWeight()
        );

        Cat a2 = maxIndex(items);

        System.out.println(a0.getWeight());
        System.out.println(a1.getWeight());
        System.out.println(a2.getWeight());
    }
}
