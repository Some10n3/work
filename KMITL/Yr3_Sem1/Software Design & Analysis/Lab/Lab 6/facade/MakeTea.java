public class MakeTea {
    public static void main(String[] args) {
        TeaCup blueCup = new TeaCup();
        TeaInfuser teaInfuser = new TeaInfuser();
        Water water = new Water();

        TeaFacade teaMaker = new TeaFacade(blueCup, teaInfuser, water);
        teaMaker.MakeTea("Earl Grey");

        TeaFacade teaMaker2 = new TeaFacade(blueCup, teaInfuser, water);
        teaMaker2.MakeTea("English Breakfast");
    }
}

