import java.util.ArrayList;
import java.util.List;

abstract class Observer {

    abstract void update();

    // Observer pulls data from the Subject
    abstract <T> T pull(Subject s);

    public static void main(String[] args) {
        
        user user = new user("John");
        follower follower1 = new follower(user);
        follower follower2 = new follower(user);

        user.addObserver(follower1);
        user.addObserver(follower2);

        user.notifyObservers();
        
        user.removeObserver(follower1);
        user.notifyObservers();

        follower1.update();
        follower2.update();

    }
}

abstract class Subject {

    private List<Observer> observers = new ArrayList<Observer>();

    public void addObserver(Observer o) {
        observers.add(o);
    }

    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    // use push mechanism to notify observers
    public void notifyObservers() {
        for (Observer o : observers) {
            o.update();
        }
    }

    // use pull mechanism to notify observers
    abstract <T> T getData();

}

class user extends Subject {

    private String name;

    public user(String name) {
        this.name = name;
    }

    @Override
    public String getData() {
        return name;
    }

}

class follower extends Observer {

    private user user;

    public follower(user user) {
        this.user = user;
    }

    @Override
    public void update() {
        System.out.println("User " + pull(user) + " has been updated");
    }

    @Override
    public String pull(Subject s) {
        return s.getData();
    }

}

