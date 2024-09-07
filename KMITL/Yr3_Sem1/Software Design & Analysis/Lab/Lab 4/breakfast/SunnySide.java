
public class SunnySide extends Eggs{
	
	public void prepareEggs() {
		System.out.println("Never stir sunny side up!");
	}
	
	public void cook() {
		System.out.println("Cooking the eggs sunny side up.");
	}

	public boolean addSaltAndPepper() {
        String answer = getUserInput();
		if (answer.equals("yes")) {
			return true;
		} else {
			return false;
		}
    }

}


