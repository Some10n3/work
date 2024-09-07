public class RecordsAdapter extends Database {
    private Records records;

    public RecordsAdapter(Records records) {
        this.records = records;
    }

    public void addEmployee(Employee employee) {
        records.insert(employee);
    }

    public void deleteEmployee(int emp_num) {
        records.remove(emp_num);
    }

    public boolean IsInDB(int emp_num) {
        return records.isEmployee(emp_num);
    }

  
}