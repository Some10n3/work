
public class Main {
    public static void main(String[] args) {
        Database DB = new Database();
        Records Records = new Records();

        Employee emp1 = new Employee("Kanokjan", "Singhsuwan", 1, 10000);
        Employee emp2 = new Employee("Teerapat", "Senanuch", 2, 20000);
        Employee emp3 = new Employee("Chanasorn", "How", 3, 30000);

        DB.addEmployee(emp1);
        Records.insert(emp2);

        
        DatabaseAdapter DBAdapter = new DatabaseAdapter(DB); //record to db
        RecordsAdapter RecordsAdapter = new RecordsAdapter(Records); //db to record


        //add employee to database and records using insert

        // DB.addEmployee(emp3);
        // RecordsAdapter.addEmployee(emp3); 

        Records.insert(emp3);
        DBAdapter.insert(emp3);
   
        DB.listall();
        Records.listall();
        
                
        System.out.println("\n-----------------");

        //remove employee from database and records using deleteEmployee
        DB.deleteEmployee(1);
        RecordsAdapter.deleteEmployee(2);

        // Records.remove(2);
        // DBAdapter.remove(1);

        DB.listall();
        Records.listall();

        
        System.out.println("\n-----------------");

        //check if employee is in database and records using isEmployee
        System.out.println("Is employee 3 in records? " + Records.isEmployee(3));
        System.out.println("Is employee 3 in Database? " + DBAdapter.isEmployee(3));

        // System.out.println("Is employee 3 in Database? " + DB.IsInDB(3));
        // System.out.println("Is employee 3 in records? " + RecordsAdapter.IsInDB(3));

    }
}