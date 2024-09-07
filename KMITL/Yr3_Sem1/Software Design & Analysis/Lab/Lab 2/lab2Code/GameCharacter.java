
public abstract class GameCharacter {
	GuitarBehavior guitarBehavior;
	SoloBehavior   soloBehavior;
	
	public GameCharacter() {
	}
	
	public void playGuitar() {
		guitarBehavior.play();
	}
	public void playSolo() {
		soloBehavior.solo();
	}
	
	public void setGuitar(GuitarBehavior g) {
		this.guitarBehavior=g;
	}
	
	public void setSolo(SoloBehavior s) {
		this.soloBehavior=s;
	}
	
	public void change() {
	}
}