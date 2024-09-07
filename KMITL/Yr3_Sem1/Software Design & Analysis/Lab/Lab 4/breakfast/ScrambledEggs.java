
public class ScrambledEggs extends Eggs{
	
	public void prepareEggs() {
		System.out.println("Stirring and adding milk to the eggs");
	}
	
	public void cook() {
		System.out.println("Scrambling the eggs.");
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


