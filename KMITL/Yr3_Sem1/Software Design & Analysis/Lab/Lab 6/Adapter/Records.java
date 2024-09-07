/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.ArrayList;

/**
 *
 * @author boonjv
 */
public class Records {

    private ArrayList<Employee> employees; //Stores the employees

    public Records() {
        employees = new ArrayList<>();
    }

    public void insert(Employee employee) {
        employees.add(employee);
    }

    public void remove(int emp_num) {
        for (Employee employee : employees) {
            if (employee.getEmpNum() == emp_num) {
                employees.remove(employee);
                break;
            }
        }
    }

    public boolean isEmployee(int emp_num) {
        for (Employee employee : employees) {
            if (employee.getEmpNum() == emp_num) {
                return true;
            }
        }
        return false;
    }

    public void listall() {
        for (Employee employee : employees) {
            System.out.println(employee.getName() + " " + employee.getSurname() + " " + employee.getEmpNum() + " " + employee.getSalary());
        }
    }
    
}
