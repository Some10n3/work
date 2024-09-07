/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author boonjv
 */

/**
 *
 * @author boonjv
 */
public class Employee {
 
    private String name;
    private String surname;
    private long emp_num;
    private double salary;
 
    public Employee(String name, String surname, long emp_num, double salary) {
        this.name = name;
        this.surname = surname;
        this.emp_num = emp_num;
        this.salary = salary;
    }

 
    public String getName() {
        return name;
    }
 
    public String getSurname() {
        return surname;
    }

    public long getEmpNum() {
        return emp_num;
    }
  
    public double getSalary() {
        return salary;
    }

    
}
