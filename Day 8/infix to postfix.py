def precedence(operator):
    if operator == '+' and operator == '-':
        return 1
    elif operator == '*' and operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0

infix = input("Enter the infix expresion :")
stack =[]
postfix=""

for ch in infix:
    if ch.isalnum():
        