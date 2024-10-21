// Handler Interface
abstract class Handler {
    protected Handler next;

    public void setNextHandler(Handler next) {
        this.next = next;
    }

    public void handleRequest(String request){
        System.out.println("Received request " + request);
    }
}

// Concrete Handlers
class SpamHandler extends Handler {
    @Override
    public void handleRequest(String request) {
        System.out.print("At SpamHandler: ");
        super.handleRequest(request);
        if (request.equalsIgnoreCase("spam")) {
            System.out.println("SpamHandler: Handling spam...\n");
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

class FanHandler extends Handler {
    @Override
    public void handleRequest(String request) {
        System.out.print("At FanHandler: ");
        super.handleRequest(request);
        if (request.equalsIgnoreCase("fan")) {
            System.out.println("FanHandler: Handling fan message...\n");
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

class ComplaintsHandler extends Handler {
    @Override
    public void handleRequest(String request) {
        System.out.print("At ComplaintsHandler: ");
        super.handleRequest(request);
        if (request.equalsIgnoreCase("complaint")) {
            System.out.println("ComplaintsHandler: Handling complaint...\n");
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

public class chainOfResponsibilitiesExample {
    public static void main(String[] args) {
        Handler spamHandler = new SpamHandler();
        Handler fanHandler = new FanHandler();
        Handler complaintsHandler = new ComplaintsHandler();

        spamHandler.setNextHandler(fanHandler);
        fanHandler.setNextHandler(complaintsHandler);

        // Test the chain
        spamHandler.handleRequest("fan");
        spamHandler.handleRequest("complaint");
        spamHandler.handleRequest("spam");
    }
}
