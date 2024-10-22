
// Bridge Pattern : decouples an abstraction from its implementation so that the two can vary independently.

// Implementor
interface Device {
    void turnOn();
    void turnOff();
}

// Concrete Implementor
class TV implements Device {
    @Override
    public void turnOn() {
        System.out.println("Turning on TV");
    }

    @Override
    public void turnOff() {
        System.out.println("Turning off TV");
    }
}

// Concrete Implementor
class Radio implements Device {
    @Override
    public void turnOn() {
        System.out.println("Turning on Radio");
    }

    @Override
    public void turnOff() {
        System.out.println("Turning off Radio");
    }
}

// Abstraction
abstract class RemoteControl {
    protected Device device;

    public RemoteControl(Device device) {
        this.device = device;
    }

    abstract void togglePower();
}

// Refined Abstraction
class BasicRemote extends RemoteControl {
    public BasicRemote(Device device) {
        super(device);
    }

    @Override
    void togglePower() {
        System.out.println("Remote: Power button pressed.");
        device.turnOn();
        device.turnOff();
    }
}

public class bridgePatternExample {
    public static void main(String[] args) {
        Device tv = new TV();
        RemoteControl remote = new BasicRemote(tv);
        remote.togglePower();
        
        Device radio = new Radio();
        remote = new BasicRemote(radio);
        remote.togglePower();
    }
}
