// Use a static variable.
class StaticDemo {
    int x; // a normal instance variable
    static int y; // a static variable

    // Return the sum of the instance variable x
    // and the static variable y.
    int sum() {
        return x + y;
    }

    static boolean isPrime(int n) {
        for (int t=2;t<n;t++) {
            if (n%t == 0) 
                return false;
        }
        return true;
    }
}

class mainn {
    public static void main(String args[]) {
        // can call isPrime without new-ing StaticDemo
        // because isPrime belongs to the class
        System.out.println("isPrime(17): " + StaticDemo.isPrime(17));
        StaticDemo ob1 = new StaticDemo();
        StaticDemo ob2 = new StaticDemo();
        // Each object has its own copy of an instance variable.
        ob1.x = 10;
        ob2.x = 20;
        System.out.println("Static.y : " + ob1.y);
        System.out.println("Of course, ob1.x and ob2.x are independent.");
        System.out.println("ob1.x: " + ob1.x + "ob2.x: " + ob2.x);
        System.out.println();
        // Each object shares one copy of a static variable.
        System.out.println("The static variable y is shared.");
        StaticDemo.y = 19; // refer to by class name
        System.out.println("Set StaticDemo.y to 19.");
        System.out.println("ob1.sum(): " + ob1.sum());
        System.out.println("ob2.sum(): " + ob2.sum());
        System.out.println();
        StaticDemo.y = 100; // refer to by class name
        System.out.println("Change StaticDemo.y to 100");
        System.out.println("ob1.sum(): " + ob1.sum());
        System.out.println("ob2.sum(): " + ob2.sum());
        System.out.println();

    }
}