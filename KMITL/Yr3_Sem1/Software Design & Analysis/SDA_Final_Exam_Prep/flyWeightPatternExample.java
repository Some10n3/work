
// Flyweight Pattern : minimize memory usage by sharing as much data as possible with similar objects.

import java.util.HashMap;
import java.util.Map;

// Flyweight interface
interface Character {
    void printCharacter();
}

// ConcreteFlyweight
class ConcreteCharacter implements Character {
    private char symbol;

    public ConcreteCharacter(char symbol) {
        this.symbol = symbol;
    }

    @Override
    public void printCharacter() {
        System.out.println("Character: " + symbol);
    }
}

// FlyweightFactory
class CharacterFactory {
    private Map<java.lang.Character, Character> characterPool = new HashMap<>();

    public Character getCharacter(char symbol) {
        // Auto-boxing 'char' to 'Character'
        java.lang.Character key = java.lang.Character.valueOf(symbol);
        Character character = characterPool.get(key);
        if (character == null) {
            character = new ConcreteCharacter(symbol);
            characterPool.put(key, character); // Explicitly convert 'char' to 'Character'
        }
        return character;
    }
}

public class flyWeightPatternExample {
    public static void main(String[] args) {
        CharacterFactory factory = new CharacterFactory();

        String document = "AAABBBCCC";
        for (char c : document.toCharArray()) {
            Character character = factory.getCharacter(c); // Auto-boxing will happen here
            character.printCharacter();
        }
    }
}