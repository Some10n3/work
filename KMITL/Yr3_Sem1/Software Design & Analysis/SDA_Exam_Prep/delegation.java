class delegation {
    public static void main(String[] args) {
        userHandler userHandler = new userHandler();
        userHandler.print();
    }
}

class userHandler {
    private user user = new user();
    
    public void print() {
        user.print();
    }
}

class user {
    public void print() {
        System.out.println("Hello, world!");
    }
}