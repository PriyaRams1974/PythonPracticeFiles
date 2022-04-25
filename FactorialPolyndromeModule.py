def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

def polyndrome(x):
   x1 = x[::-1]
   if x == x1:
       print(x, "is a polyndrome no")
   else:
       print(x, "is not a polyndrome no")

