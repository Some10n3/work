public class FanHandler extends Handler {

    public FanHandler() {
        super();
    }

    public FanHandler(Handler nextHandler) {
        super(nextHandler);
    }

    public void handleRequest(int request) {
        System.out.println("FanHandler recieved request : " + request);
        if (request == 2) {
            System.out.println("FanHandler: Handling request " + request + "\n");
        } else {
            super.handleRequest(request);
        }
    }
}
