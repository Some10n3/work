
public class GameCharacterAngus extends GameCharacter {
	
	
	public GameCharacterAngus() {
		 guitarBehavior=new Guitar_GibsonLP();
		 soloBehavior=new Solo_SmashTheGuitar();
	}

    public void change() {
        this.setGuitar(new Guitar_Telecaster());
    }
}
