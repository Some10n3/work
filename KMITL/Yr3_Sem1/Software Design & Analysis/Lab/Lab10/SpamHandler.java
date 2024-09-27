public class SpamHandler extends Handler {

    public SpamHandler() {
        super();
    }

    public SpamHandler(Handler nextHandler) {
        super(nextHandler);
    }

    public void handleRequest(int request) {
        System.out.println("SpamHandler recieved request : " + request);
        if (request == 1) {
            System.out.println("SpamHandler: Handling request " + request + "\n");
        } else {
            super.handleRequest(request);
        }
    }
}

