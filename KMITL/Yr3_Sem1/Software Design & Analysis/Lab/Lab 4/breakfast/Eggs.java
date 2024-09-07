import java.util.Scanner;

public abstract class Eggs {

    public void prepareRecipe() {
        crackingEggs(2);
        prepareEggs();
        cook();
        serve();
    }

    final void crackingEggs(int n) {
        System.out.println("Cracking " + n + " eggs.");
    }
    
    abstract void prepareEggs();
    
    abstract void cook();
    
    final void serve() {
        System.out.println("Serving the eggs");
    }

    public boolean addSaltAndPepper() {
        return true;
    }

    public String getUserInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Would you like to add salt and pepper?");
        String answer = scanner.nextLine();
        scanner.close();
        return answer;
    }

}


