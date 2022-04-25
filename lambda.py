# lambda function
# add = lambda x: x + 10
# print(add(5))
# ==================
# def add_number(x) :
#     return x + 10
# print(add_number(5))
# ==================
# lambda multiplication
# mult = lambda x, y: x * y
# print(mult(5, 6))
# ==================
# sorted method default with x
# points2D = [(1, 3), (5, 7), (-4, 1), (-7, 10)]
# points2D_SORTED = sorted(points2D)
# print("points2D ==>", points2D)
# print("points2D_SORTED ==>", points2D_SORTED)
# ===============
# map function
# a = [1, 2, 3, 4, 5]
# b = map(lambda x:x+2, a)
# print(list(b))
# ===============
# list comprehension
# a = [1, 2, 3, 4, 5]
# c = [x*2 for x in a]
# print(c)
# ===============
# filter function
# a = [1, 2, 3, 4, 5]
# b = filter(lambda x: x % 2 == 0, a)
# print(list(b))
# ===============
# list comprehension
# a = [1, 2, 3, 4, 5]
# c = [x for x in a if x % 2 == 0]
# print(c)
# ===========
# reduce function
# #from functools import reduce
# a = [1, 2, 3, 4, 5]
# product_a = reduce(lambda x, y : x*y, a)
# print("product_a ==>", product_a)
# ===========
# reduce function to find factorial of a number
from functools import reduce
# find factorial of 5
n = int(input("Enter the number to find Factorial "))
mylist = []
for i in range(1, n + 1):
    mylist.append(i)
Factorial = reduce(lambda x, y: x * y, mylist)
print("Factorial of ", n, "==>", Factorial)
