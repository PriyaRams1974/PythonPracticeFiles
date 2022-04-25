# Enter the number for the multiplication
number = input("Enter the number : ")

i = 1
value = number
while i <= 10:
    # value = value + int(number)
    print(int(value),' * ', i,' = ',int(value) * int(i))
    i = i + 1

j = 1
value1 = 5
while j <= 10:
    # value = value + int(number)
    print(value1, ' * ', j, ' = ', (value1*j))
    j = j + 1