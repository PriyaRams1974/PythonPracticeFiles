number = int(input("Enter the number to be checked for Prime no : "))
x = True
for i in range(2, number-1):
    if (number % i == 0):
        x = False
        break
if (x == False) :
    print(number, "is not a Prime no")
else:
    print(number, "is a Prime no")

