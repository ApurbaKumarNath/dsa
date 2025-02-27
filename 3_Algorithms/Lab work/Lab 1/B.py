T = int(input())
for i in range(T):
    arr = input().split()
    string, operand1, operator, operand2 = arr
    if operator == '+':
        result = int(operand1) + int(operand2)
    elif operator == '-':
        result = int(operand1) - int(operand2)
    elif operator == '*':
        result = int(operand1) * int(operand2)
    elif operator == '/':
        result = int(operand1) / int(operand2)
    print(result)