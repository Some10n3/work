package code;

import java.util.Arrays;

public class Puzzle8State {
    public int[] sequence;

    public Puzzle8State(int[] sequence) {
        this.sequence = sequence;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Puzzle8State that = (Puzzle8State) obj;
        return Arrays.equals(sequence, that.sequence);
    }

    @Override
    public int hashCode() {
        return Arrays.hashCode(sequence);
    }

    @Override
    public String toString() {
        return Arrays.toString(sequence);
    }
}
