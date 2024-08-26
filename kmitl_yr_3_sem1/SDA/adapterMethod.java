class AdapterMethod{
    public static void main(String[] args) {
        StudentFromKMITL neo = new StudentFromKMITL();
        StudentFromMUIC jane = new StudentFromMUIC();

        neo.setName("Neo");
        jane.setName("Jane");

        neo.doAssignment();
        jane.workOnAssignment();

        MUICtoKMITLAdapter muicToKMITLAdapter = new MUICtoKMITLAdapter(jane);
        System.out.print(muicToKMITLAdapter.getName() + " ");
        muicToKMITLAdapter.doAssignment();

        KMITLtoMUICAdapter kmitlToMUICAdapter = new KMITLtoMUICAdapter(neo);
        System.out.print(kmitlToMUICAdapter.getName() + " ");
        kmitlToMUICAdapter.workOnAssignment();
    }
}

abstract class Student{
    String name;
    int id;

    public abstract void study();
    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }
}

class StudentFromKMITL extends Student{
    public void study(){
        System.out.println("Study at KMITL");
    }

    public void doAssignment(){
        System.out.println("Do assignment");
    }

}

class StudentFromMUIC extends Student{
    public void study(){
        System.out.println("Study at MUIC");
    }

    public void workOnAssignment(){
        System.out.println("Work on assignment");
    }
}

class MUICtoKMITLAdapter extends StudentFromKMITL{
    StudentFromMUIC studentFromMUIC;

    public MUICtoKMITLAdapter(StudentFromMUIC studentFromMUIC){
        this.studentFromMUIC = studentFromMUIC;
    }

    public String getName(){
        return studentFromMUIC.name;
    }

    public void doAssignment(){
        studentFromMUIC.workOnAssignment();
    }
}

class KMITLtoMUICAdapter extends StudentFromMUIC{
    StudentFromKMITL studentFromKMITL;

    public KMITLtoMUICAdapter(StudentFromKMITL studentFromKMITL){
        this.studentFromKMITL = studentFromKMITL;
    }

    public String getName(){
        return studentFromKMITL.name;
    }

    public void workOnAssignment(){
        studentFromKMITL.doAssignment();
    }
}