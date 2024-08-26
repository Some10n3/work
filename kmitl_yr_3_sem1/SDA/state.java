// Client code
public class State {
    public static void main(String[] args) {
        VendingMachine machine = new VendingMachine();

        machine.insertCoin();
        machine.selectProduct();
        machine.dispense();

        machine.selectProduct(); // Should return to NoCoinState after dispensing
        machine.insertCoin();
        machine.selectProduct();
        machine.dispense();
    }
}

// State interface
interface VendingMachineState {
    void insertCoin();
    void selectProduct();
    void dispense();
}

// ConcreteState: NoCoinState
class NoCoinState implements VendingMachineState {
    private VendingMachine machine;

    public NoCoinState(VendingMachine machine) {
        this.machine = machine;
    }

    @Override
    public void insertCoin() {
        System.out.println("Coin inserted.");
        machine.setState(machine.getHasCoinState());
    }

    @Override
    public void selectProduct() {
        System.out.println("Insert a coin first.");
    }

    @Override
    public void dispense() {
        System.out.println("Insert a coin first.");
    }
}

// ConcreteState: HasCoinState
class HasCoinState implements VendingMachineState {
    private VendingMachine machine;

    public HasCoinState(VendingMachine machine) {
        this.machine = machine;
    }

    @Override
    public void insertCoin() {
        System.out.println("Coin already inserted.");
    }

    @Override
    public void selectProduct() {
        System.out.println("Product selected.");
        machine.setState(machine.getDispensingState());
    }

    @Override
    public void dispense() {
        System.out.println("Select a product first.");
    }
}

// ConcreteState: DispensingState
class DispensingState implements VendingMachineState {
    private VendingMachine machine;

    public DispensingState(VendingMachine machine) {
        this.machine = machine;
    }

    @Override
    public void insertCoin() {
        System.out.println("Please wait, dispensing product.");
    }

    @Override
    public void selectProduct() {
        System.out.println("Please wait, dispensing product.");
    }

    @Override
    public void dispense() {
        System.out.println("Product dispensed.");
        machine.setState(machine.getNoCoinState());
    }
}

// Context: VendingMachine
class VendingMachine {
    private VendingMachineState noCoinState;
    private VendingMachineState hasCoinState;
    private VendingMachineState dispensingState;

    private VendingMachineState currentState;

    public VendingMachine() {
        noCoinState = new NoCoinState(this);
        hasCoinState = new HasCoinState(this);
        dispensingState = new DispensingState(this);

        currentState = noCoinState;
    }

    public void setState(VendingMachineState state) {
        this.currentState = state;
    }

    public VendingMachineState getNoCoinState() {
        return noCoinState;
    }

    public VendingMachineState getHasCoinState() {
        return hasCoinState;
    }

    public VendingMachineState getDispensingState() {
        return dispensingState;
    }

    public void insertCoin() {
        currentState.insertCoin();
    }

    public void selectProduct() {
        currentState.selectProduct();
    }

    public void dispense() {
        currentState.dispense();
    }
}
