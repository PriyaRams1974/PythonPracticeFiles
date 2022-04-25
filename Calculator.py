# 2 , 3
Operand1 = input("Enter operand1 : ")
Operand2 = input("Enter operand2 : ")

# + - * /
validOperator = False
while not validOperator:
    Operator = input("Enter the Operator : ")
    if Operator == '+' or Operator == '-' or Operator == '*' or Operator == '/':
        validOperator = True
    else:
        print("Please enter valid Operator")

# Program Logic
Result = 0.0;
Valid = True
if Operator == '+':
    Result = float(Operand1) + float(Operand2)
elif Operator == '-':
    Result = float(Operand1) - float(Operand2)
elif Operator == '*':
    Result = float(Operand1) * float(Operand2)
elif Operator == '/':
    Result = float(Operand1) / float(Operand2)
else:
    Valid = False
    print( "Invalid Operator")

if Valid:
    print("Result is ", str(Result))
else:
    print("Nothing to compute - Invalid State of Calculator")