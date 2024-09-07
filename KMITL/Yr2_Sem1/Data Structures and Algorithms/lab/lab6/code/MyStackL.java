package code;
public class MyStackL {
    int MAX_SIZE=100;
    String stack[] = new String[MAX_SIZE];
    int top = 0;

    public void push(String d) {
        stack[top++] = d;
    }
    
    public String pop() {
        if(!isEmpty()) return stack[--top];
        else return "Stack is empty";
    }

    public String top() {
        if(!isEmpty()) return stack[top-1];
        else return "Stack is empty";
    }

    public boolean isFull() {
        return top==MAX_SIZE;
    }
    
    public boolean isEmpty() {
        return top==0;
    }
    
    public String peek() {
        if(!isEmpty()) return stack[top-1];
        else return "Stack is empty";
    }

    public String toString() {
        StringBuffer sb = new StringBuffer();
        sb.append("top->");
        for(int i=top-1; i>=0; i--) {
            sb.append("[");
            sb.append(stack[i]);
            sb.append("]->");
        }
       sb.append("bottom");
        return new String(sb);
    }
}