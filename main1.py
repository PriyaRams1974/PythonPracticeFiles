# import  CalculatorModule as c
# print(c.add(5,10))
# print(c.subtract(5,10))
# print(c.multiply(5,10))
# print(c.divide(5,10))
# ======================
# from CalculatorModule import add
# print(add(5, 7))
# ===========================
# import FactorialPolyndromeModule as fs
# print(fs.fact(5))
# print(fs.polyndrome('12321'))
# ===========================
# from FactorialPolyndromeModule import *
# print(fact(5))
# print(polyndrome('12321'))
# ===========================
import sys
print(sys.path)

import platform
print(platform.system())
print(dir(platform))

import math
print(math.factorial(5))

import random
print(random.random())
print(random.uniform(1, 10))
print(random.randint(1,10)) # include end boundary
print(random.randrange(1, 10)) # exclude end boundary

mylist = list("ABCDEF")
print(mylist)
print(random.choice(mylist))
print(random.sample(mylist, 3))
print(random.choices(mylist, k=3)) # duplicate element

