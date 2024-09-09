package examples;

import java.util.Stack;

public class stack {
    
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        
        //methods : push, pop, peek, empty, search, clear
        
        stack.push(1);
        stack.push(2);
        stack.push(3);
        
        System.out.println(stack); // [1, 2, 3]
        
        System.out.println(stack.pop()); // 3
        
        System.out.println(stack); // [1, 2]
        
        System.out.println(stack.peek()); // 2
        
        System.out.println(stack.empty()); // false
        
        System.out.println(stack.search(1)); // 2

        stack.clear();

        System.out.println(stack.empty()); // true

        //Iterating through a stack

        stack.push(1);
        stack.push(2);
        stack.push(3);

        for (Integer i : stack) {
            System.out.println(i);
        }
    }
}
