import java.util.ArrayList;
import java.util.List;

// Custom TwitterAccount class
class TwitterAccount {
    // observers
    private List<Follower> followers = new ArrayList<>();
    private String tweet;

    // Method to add a follower (observer)
    public void addFollower(Follower follower) {
        followers.add(follower);
    }

    // Method to remove a follower (observer)
    public void removeFollower(Follower follower) {
        followers.remove(follower);
    }

    // Method to post a new tweet (push mechanism)
    public void postTweet(String tweet) {
        this.tweet = tweet;
        notifyFollowers(); // Notify all followers
    }

    // Notify all followers
    private void notifyFollowers() {
        for (Follower follower : followers) {
            follower.update(this);
        }
    }

    // Retrieve the latest tweet (pull mechanism)
    public String getLatestTweet() {
        return tweet;
    }

     public static void main(String[] args) {
        TwitterAccount account = new TwitterAccount();
        Follower follower1 = new Follower("Alice");
        Follower follower2 = new Follower("Bob");

        account.addFollower(follower1); // Alice follows the account
        account.addFollower(follower2); // Bob follows the account

        // The Twitter account posts a new tweet
        account.postTweet("Hello, world! This is my first tweet!");
    }
}

// Custom Follower class
class Follower {
    private String name;

    public Follower(String name) {
        this.name = name;
    }

    public void update(TwitterAccount account) {
        String latestTweet = account.getLatestTweet();
        System.out.println(name + " received a new tweet: " + latestTweet);
    }
}