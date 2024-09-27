public class NewLocationHandler extends Handler {

    public NewLocationHandler() {
        super();
    }

    public NewLocationHandler(Handler nextHandler) {
        super(nextHandler);
    }

    public void handleRequest(int request) {
        System.out.println("NewLocationHandler recieved request : " + request);
        if (request == 4) {
            System.out.println("NewLocationHandler: Handling request " + request + "\n");
        } else {
            super.handleRequest(request);
        }
    }
    
}
