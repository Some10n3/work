import java.util.List;
import java.util.LinkedList;

public class TestGuitarHero {

    public static void CharPlay(List<GameCharacter> players) {
        for (GameCharacter player : players) {
            player.playGuitar();
            player.playSolo();
        }
    }

	public static void main(String[] args) {
			GameCharacter player1 = new GameCharacterSlash();
			GameCharacter player2 = new GameCharacterHendrix();
            GameCharacter player3 = new GameCharacterAngus();

			
            List<GameCharacter> players = new LinkedList<GameCharacter>();
            System.out.println("First Test!");
            players.add(player1);
            players.add(player2);
            players.add(player3);
			CharPlay(players);
			
            System.out.println("Second Test! (after change)");
			player1.change();
            player3.change();
            CharPlay(players);
		}
	}

