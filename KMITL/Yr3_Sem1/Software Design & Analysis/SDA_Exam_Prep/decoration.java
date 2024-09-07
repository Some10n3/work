abstract class decoration {
    public static void main(String[] args) {
        Bagel bagel = new BasicBagel();
        System.out.println(bagel.getDescription() + " $" + bagel.cost());

        Bagel bagel2 = new BasicBagel();
        bagel2 = new creamCheese(bagel2);
        bagel2 = new smokedSalmon(bagel2);
        System.out.println(bagel2.getDescription() + " $" + bagel2.cost());

        Bagel bagel3 = new SesameBagel();
        bagel3 = new creamCheese(bagel3);
        bagel3 = new smokedSalmon(bagel3);
        bagel3 = new smokedSalmon(bagel3);
        System.out.println(bagel3.getDescription() + " $" + bagel3.cost());

    }
}

abstract class Bagel {
    public abstract String getDescription();
    public abstract double cost();
}

// The basic Bagel class that extends the abstract Bagel
class BasicBagel extends Bagel {
    private String description;

    public BasicBagel() {
        this.description = "Bagel";
    }

    @Override
    public String getDescription() {
        return description;
    }

    @Override
    public double cost() {
        return 0.5;
    }
}

class SesameBagel extends Bagel {
    private String description;

    public SesameBagel() {
        this.description = "Sesame Bagel";
    }

    @Override
    public String getDescription() {
        return description;
    }

    @Override
    public double cost() {
        return 0.75;
    }
}

// The BagelDecorator abstract class that extends Bagel
abstract class BagelDecorator extends Bagel {
    protected Bagel bagel;

    public BagelDecorator(Bagel bagel) {
        this.bagel = bagel;
    }

    @Override
    public abstract String getDescription();
}

// Cream Cheese decorator class
class creamCheese extends BagelDecorator {
    public creamCheese(Bagel bagel) {
        super(bagel);
    }

    @Override
    public String getDescription() {
        return bagel.getDescription() + ", Cream Cheese";
    }

    @Override
    public double cost() {
        return bagel.cost() + 0.5;
    }
}

// Smoked Salmon decorator class
class smokedSalmon extends BagelDecorator {
    public smokedSalmon(Bagel bagel) {
        super(bagel);
    }

    @Override
    public String getDescription() {
        return bagel.getDescription() + ", Smoked Salmon";
    }

    @Override
    public double cost() {
        return bagel.cost() + 1.5;
    }
}
