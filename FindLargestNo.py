
a = input("Enter operand1 : ")
b = input("Enter operand2 : ")
c = input("Enter operand3 : ")

a = int(a)
b = int(b)
c = int(c)

if((a>b and a>c) and (a != b and a != c)):
    print(a, " is the largest")
elif((b>a and b>c) and (b != a and b != c)):
    print(b, " is the largest")
elif((c>a and c>b) and (c != a and c != b)):
    print(c, " is the largest")
else:
    print("entered numbers are equal")
