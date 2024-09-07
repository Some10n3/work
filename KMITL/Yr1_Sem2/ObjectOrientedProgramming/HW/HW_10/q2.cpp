#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>

using namespace std;

// Function to check if a character is an operator
bool isOperator(char c) {
    return c == '~' || c == '&' || c == '|' || c == '^';
}

// Function to evaluate bitwise logical expressions
int evaluateExpression(const string& expression) {
    stack<int> operandStack;
    stack<char> operatorStack;
    unordered_map<char, int> precedence{{'~', 3}, {'&', 2}, {'|', 1}, {'^', 0}};

    for (char c : expression) {
        if (c == ' ') {
            continue;  // Ignore spaces
        } else if (isOperator(c)) {
            while (!operatorStack.empty() && precedence[c] < precedence[operatorStack.top()]) {
                char op = operatorStack.top();
                operatorStack.pop();

                int operand2 = operandStack.top();
                operandStack.pop();

                if (op == '~') {
                    operandStack.push(~operand2);
                } else {
                    int operand1 = operandStack.top();
                    operandStack.pop();
                    switch (op) {
                        case '&':
                            operandStack.push(operand1 & operand2);
                            break;
                        case '|':
                            operandStack.push(operand1 | operand2);
                            break;
                        case '^':
                            operandStack.push(operand1 ^ operand2);
                            break;
                    }
                }
            }
            operatorStack.push(c);
        } else {
            int operand = c - '0';  // Convert character to integer
            operandStack.push(operand);
        }
    }

    while (!operatorStack.empty()) {
        char op = operatorStack.top();
        operatorStack.pop();

        int operand2 = operandStack.top();
        operandStack.pop();

        if (op == '~') {
            operandStack.push(~operand2);
        } else {
            int operand1 = operandStack.top();
            operandStack.pop();
            switch (op) {
                case '&':
                    operandStack.push(operand1 & operand2);
                    break;
                case '|':
                    operandStack.push(operand1 | operand2);
                    break;
                case '^':
                    operandStack.push(operand1 ^ operand2);
                    break;
            }
        }
    }

    return operandStack.top();
}

int main() {
    string expression;
    cout << "Enter a bitwise logical expression: ";
    getline(cin, expression);

    int result = evaluateExpression(expression);
    cout << "Result: " << result << endl;
    getline(cin, expression);

    return 0;
}
