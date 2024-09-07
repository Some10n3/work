
public class EatBreakfast {
	public static void main(String[] args) {
		ScrambledEggs scrambled = new ScrambledEggs();
		scrambled.crackingEggs(2);
		scrambled.prepareEggs();
		scrambled.cook();
		scrambled.serve();
		
		Omelette omelette = new Omelette();
		omelette.crackingEggs(3);
		omelette.prepareEggs();
		omelette.cook();
		omelette.serve();
		
		SunnySide sunny = new SunnySide();
		sunny.crackingEggs(1);
		sunny.prepareEggs();
		sunny.cook();
		sunny.serve();
	}

}

