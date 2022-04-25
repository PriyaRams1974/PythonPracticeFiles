

def calculator(Operand1,Operand2,Operator):
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        validOperator = True
        if Operator == '+':
            Result = int(Operand1) + int(Operand2)
        elif Operator == '-':
            Result = int(Operand1) - int(Operand2)
        elif Operator == '*':
            Result = int(Operand1) * int(Operand2)
        elif Operator == '/':
            Result = int(Operand1) / int(Operand2)
        print(Operand1, ' ', Operator, ' ', Operand2, ' = ', Result)
    else:
        print("Please enter valid Operator")

Operand1 = int(input("Enter operand1 : "))
Operand2 = int(input("Enter operand2 : "))
operation = input("Enter operation : ")
calculator(Operand1, Operand2, operation)
