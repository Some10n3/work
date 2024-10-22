// Product class with complex structure
class House {
    private String foundation;
    private String structure;
    private String roof;

    public void setFoundation(String foundation) {
        this.foundation = foundation;
    }

    public void setStructure(String structure) {
        this.structure = structure;
    }

    public void setRoof(String roof) {
        this.roof = roof;
    }

    @Override
    public String toString() {
        return "House with foundation: " + foundation + ", structure: " + structure + ", roof: " + roof;
    }
}

// Builder interface
interface HouseBuilder {
    void buildFoundation();
    void buildStructure();
    void buildRoof();
    House getHouse();
}

// Concrete Builder class
class ConcreteHouseBuilder implements HouseBuilder {
    private House house;

    public ConcreteHouseBuilder() {
        this.house = new House();
    }

    @Override
    public void buildFoundation() {
        house.setFoundation("Concrete foundation");
    }

    @Override
    public void buildStructure() {
        house.setStructure("Concrete and brick structure");
    }

    @Override
    public void buildRoof() {
        house.setRoof("Concrete roof");
    }

    @Override
    public House getHouse() {
        return house;
    }
}

class WoodenHouseBuilder implements HouseBuilder {
    private House house;

    public WoodenHouseBuilder() {
        this.house = new House();
    }

    @Override
    public void buildFoundation() {
        house.setFoundation("Wooden foundation");
    }

    @Override
    public void buildStructure() {
        house.setStructure("Wooden structure");
    }

    @Override
    public void buildRoof() {
        house.setRoof("Wooden roof");
    }

    @Override
    public House getHouse() {
        return house;
    }
}

// Director class
class Architect {
    private HouseBuilder builder;

    public Architect(HouseBuilder builder) {
        this.builder = builder;
    }

    public void constructHouse() {
        builder.buildFoundation();
        builder.buildStructure();
        builder.buildRoof();
    }

    public House getHouse() {
        return builder.getHouse();
    }
}

// Example usage
public class builderPatternExample {
    public static void main(String[] args) {
        HouseBuilder builder = new ConcreteHouseBuilder();
        Architect architect = new Architect(builder);

        architect.constructHouse();
        House house = architect.getHouse();

        System.out.println(house);  // Output: House with foundation: Concrete foundation, structure: Concrete and brick structure, roof: Concrete roof

        builder = new WoodenHouseBuilder();
        architect = new Architect(builder);

        architect.constructHouse();
        house = architect.getHouse();

        System.out.println(house);  // Output: House with foundation: Wooden foundation, structure: Wooden structure, roof: Wooden roof
    }
}
