public class Facade {
    public static void main(String[] args) {
        // Create the facade
        LightFacade lightFacade = new LightFacade();

        // Use the facade to control the lights
        lightFacade.turnAllLightsOn();
        lightFacade.turnAllLightsOff();
    }
}


// Subsystem classes
class LivingRoomLight {
    public void on() {
        System.out.println("Living Room Light is ON");
    }

    public void off() {
        System.out.println("Living Room Light is OFF");
    }
}

class KitchenLight {
    public void on() {
        System.out.println("Kitchen Light is ON");
    }

    public void off() {
        System.out.println("Kitchen Light is OFF");
    }
}

class BedroomLight {
    public void on() {
        System.out.println("Bedroom Light is ON");
    }

    public void off() {
        System.out.println("Bedroom Light is OFF");
    }
}

// Facade class
class LightFacade {
    private LivingRoomLight livingRoomLight;
    private KitchenLight kitchenLight;
    private BedroomLight bedroomLight;

    public LightFacade() {
        this.livingRoomLight = new LivingRoomLight();
        this.kitchenLight = new KitchenLight();
        this.bedroomLight = new BedroomLight();
    }

    public void turnAllLightsOn() {
        livingRoomLight.on();
        kitchenLight.on();
        bedroomLight.on();
    }

    public void turnAllLightsOff() {
        livingRoomLight.off();
        kitchenLight.off();
        bedroomLight.off();
    }
}