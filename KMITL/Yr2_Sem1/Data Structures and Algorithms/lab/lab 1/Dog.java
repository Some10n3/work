public class Dog {
  private String breed;
  private int magicValue;
  
  public Dog(String n){
    breed = n;
    int v = 0;
    for(int i = 0; i < n.length(); i++){
      v += n.charAt(i);
    }
    magicValue = v;
  }

  @Override
  public String toString(){
    return breed + "(" + magicValue + ")";
  }

  public boolean equals(Dog n){
    return this.breed == n.breed;
  }

  public String getBreed(){
    return breed;
  }

  public int getmagicValue(){
    return magicValue;
  }
}
