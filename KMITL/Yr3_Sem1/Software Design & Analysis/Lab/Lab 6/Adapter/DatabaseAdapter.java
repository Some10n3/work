public class DatabaseAdapter extends Records {
    private Database database;

    public DatabaseAdapter(Database database) {
        this.database = database;
    }

    public void insert(Employee employee) {
        database.addEmployee(employee);
    }

    public void remove(int emp_num) {
        database.deleteEmployee(emp_num);
    }

    public boolean isEmployee(int emp_num) {
        return database.IsInDB(emp_num);
    }

}
