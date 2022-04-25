# Fibonacci Series
limit = input("Enter limit : ")
limit = int(limit)

n1 = 0
n2 = 1
i = 0
i = int(i)
value = 0
value = int(value)

n1 = int(n1)
n2 = int(n2)
print('Fibonacci series using while loop')
print(0, 1, end=" ")
while (i<limit):
    value = n1 + n2
    print(value, end=" ")
    n1 = n2
    n2 = value
    i += 1

