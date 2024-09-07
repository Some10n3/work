// Command Interface
interface Command {
    void execute();

    public static void main(String[] args) {
        // Create the receiver objects
        Light livingRoomLight = new Light();
        Fan ceilingFan = new Fan();

        // Create the command objects
        Command lightOn = new LightOnCommand(livingRoomLight);
        Command lightOff = new LightOffCommand(livingRoomLight);
        Command fanOn = new FanOnCommand(ceilingFan);
        Command fanOff = new FanOffCommand(ceilingFan);

        // Create the invoker object
        RemoteControl remote = new RemoteControl();

        // Execute commands
        remote.setCommand(lightOn);
        remote.pressButton(); // The light is on

        remote.setCommand(fanOn);
        remote.pressButton(); // The fan is on

        remote.setCommand(fanOff);
        remote.pressButton(); // The fan is off

        remote.setCommand(lightOff);
        remote.pressButton(); // The light is off
    }
}

// Receiver classes
class Light {
    public void on() {
        System.out.println("The light is on");
    }
    
    public void off() {
        System.out.println("The light is off");
    }
}

class Fan {
    public void on() {
        System.out.println("The fan is on");
    }
    
    public void off() {
        System.out.println("The fan is off");
    }
}

// Concrete Command classes
class LightOnCommand implements Command {
    private Light light;

    public LightOnCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.on();
    }
}

class LightOffCommand implements Command {
    private Light light;

    public LightOffCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.off();
    }
}

class FanOnCommand implements Command {
    private Fan fan;

    public FanOnCommand(Fan fan) {
        this.fan = fan;
    }

    @Override
    public void execute() {
        fan.on();
    }
}

class FanOffCommand implements Command {
    private Fan fan;

    public FanOffCommand(Fan fan) {
        this.fan = fan;
    }

    @Override
    public void execute() {
        fan.off();
    }
}

// Invoker class
class RemoteControl {
    private Command command;

    public void setCommand(Command command) {
        this.command = command;
    }

    public void pressButton() {
        command.execute();
    }
}