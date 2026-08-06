def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0

infix = input("Enter the infix expresion :")
stack =[]
postfix=""

for ch in infix:
    if ch.isalnum():
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()

    else:
        while stack and precedence(stack[-1]) >= precedence(ch):
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

print("Postfix Expression:", postfix)