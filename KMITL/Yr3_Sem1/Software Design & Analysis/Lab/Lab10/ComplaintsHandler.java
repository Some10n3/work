public class ComplaintsHandler extends Handler {

    public ComplaintsHandler() {
        super();
    }

    public ComplaintsHandler(Handler nextHandler) {
        super(nextHandler);
    }
    
    public void handleRequest(int request) {
        System.out.println("ComplaintsHandler recieved request : " + request);
        if (request == 3) {
            System.out.println("ComplaintsHandler: Handling request " + request + "\n");
        } else {
            super.handleRequest(request);
        }
    }
    
}
