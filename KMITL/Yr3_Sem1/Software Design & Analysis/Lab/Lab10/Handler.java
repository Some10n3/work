public class Handler {

    private Handler nextHandler;

    public Handler() {
        this.nextHandler = null;
    }

    public Handler(Handler nextHandler) {
        this.nextHandler = nextHandler;
    }

    public void setNextHandler(Handler nextHandler) {
        this.nextHandler = nextHandler;
    }

    public void handleRequest(int request) {
        if (nextHandler != null) {
            System.out.println("Incompatible, sending request to Handler : " + nextHandler.getClass().getName());
            nextHandler.handleRequest(request);
        }
    }

    public void identifyHandler() {
        System.out.println(this.getClass().getName());
    }


    public static void main(String[] args) {
        chainOfResponsibility chain = new chainOfResponsibility();
        chain.makeRequest(1);
        chain.makeRequest(2);
        chain.makeRequest(3);
        chain.makeRequest(4);
    }
}

class chainOfResponsibility {
    
    Handler handlerChain;

    public chainOfResponsibility() {
        buildChain();
    }

    private void buildChain() {
        handlerChain = new SpamHandler(new FanHandler(new ComplaintsHandler(new NewLocationHandler())));
    }

    public void makeRequest(int request) {
        handlerChain.handleRequest(request);
    }

}