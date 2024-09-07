def validate_Brackets(length, str):
    stack = []
    for i in range(length):
        if str[i] == '(' or str[i] == '[' or str[i] == '{':
            stack.append(str[i])
        elif str[i] == ')' or str[i] == ']' or str[i] == '}':
            if len(stack) == 0:
                return "Invalid"
            top = stack.pop()
            if (top == '(' and str[i] != ')') or (top == '[' and str[i] != ']') or (top == '{' and str[i] != '}'):
                return "Invalid"
    if len(stack) != 0:
        return "Invalid"
    return "Valid"

length = int(input())
str = input()
print(validate_Brackets(length, str))




















