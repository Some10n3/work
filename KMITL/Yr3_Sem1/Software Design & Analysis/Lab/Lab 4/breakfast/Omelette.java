
public class Omelette extends Eggs{
	
	public void prepareEggs() {
		System.out.println("Stirring the eggs");
	}
	
	public void cook() {
		System.out.println("Flipping the omelette while cooking");
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

