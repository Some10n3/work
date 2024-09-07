public class TeaFacade {
    private TeaCup teaCup;
    private TeaInfuser infuser;
    private Water water;

    public TeaFacade(TeaCup teaCup, TeaInfuser infuser, Water water) {
        this.teaCup = teaCup;
        this.infuser = infuser;
        this.water = water;
    }

    public void MakeTea(String TeaType) {
        Tea tea = new Tea(TeaType);
        infuser.addTea(tea);
        water.boilWater();
        teaCup.addWater(water);
        teaCup.setSteepTime(15);
        teaCup.steep();
    }
}