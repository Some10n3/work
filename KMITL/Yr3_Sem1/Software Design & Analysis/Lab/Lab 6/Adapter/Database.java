/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author boonjv
 */
import java.util.Vector;

/**
 *
 * @author boonjv
 */
public class Database {

    private Vector<Employee> employees; //Stores the employees

    public Database() {
        employees = new Vector<>();
    }

    public void addEmployee(Employee employee) {
        employees.add(employee);
    }

    public void deleteEmployee(int emp_num) {
        for (Employee employee : employees) {
            if (employee.getEmpNum() == emp_num) {
                employees.remove(employee);
                break;
            }
        }
    }

    public void listall() {
        for (Employee employee : employees) {
            System.out.println(employee.getName() + " " + employee.getSurname() + " " + employee.getEmpNum() + " " + employee.getSalary());
        }
    }

    public boolean IsInDB(int emp_num) {
        for (Employee employee : employees) {
            if (employee.getEmpNum() == emp_num) {
                return true;
            }
        }
        return false;
    }

}
