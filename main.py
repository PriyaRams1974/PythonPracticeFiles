# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Different types of sets in Python
# set of integers
# my_set = {1, 2, 3}
# print(my_set)
#
# # set of mixed datatypes
# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)
# my_set.add((1, 2, 3))
# print(my_set)
# # my_set.add({1, 2, 3})
# # print(my_set)
# my_set.add((1, 2, 3, 3))
# print(my_set)
# my_set.add((1, 2, 3, 3))
# print(my_set)
# my_set.add((1, 2, 3, 3))
# print(my_set)
#
# # =========================
#
# myset = set()
# obj1 = {1, 2}
# myset.update(obj1)
# obj2 = {2, 3}
# myset.update(obj2)
# obj3 = {2, 4}
# myset.update(obj3)
# obj4 = {2, 5}
# myset.update(obj4)
# obj5 = {2, "hello"}
# myset.update(obj5)
# print(myset)
# #===============
#
# myset1 = set()
# obj1 = (1, 2)
# myset1.update(obj1)
# obj2 = (2, 3)
# myset1.update(obj2)
# obj3 = (2, 4)
# myset1.update(obj3)
# obj4 = (2, 5)
# myset1.update(obj4)
# obj5 = {2, "hello1"}
# myset1.update(obj5)
# print(myset1)
#
# myset2 = set()
# obj1 = (1, 2)
# myset2.add(obj1)
# obj2 = (2, 3)
# myset2.add(obj2)
# obj3 = (2, 4)
# myset2.add(obj3)
# obj4 = (2, 5)
# myset2.add(obj4)
# obj5 = (2, "hello13")
# myset2.add(obj5)
# print(myset2)

my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
# my_set = {1.0, "Hello", (1, 2, 3)}
my_set = set()

print(my_set)
# my_set.add((1, 2, 3))
# print(my_set)
# # my_set.add({1, 2, 3})
# # print(my_set)
# my_set.add((1, 2, 3, 3))
# print(my_set)
# my_set.add((1, 2, 3, 3))
# print(my_set)
my_set = set()
print(my_set)
my_set.add((1,2,3,3,3,3,3,3))
print(my_set)
my_set = {"a", "b", "c", "d", "A", "G", "H"}
print(my_set.pop())

my_set1 = {1,2,3,4,5,6}
print(my_set1.pop())

# test_set = set("geEks")
#
# # Iterating using enumerated for loop
# for id, val in enumerate(test_set):
#     print(id, val)

    # set1 = {1, 2, 3, 4}
    #
    # # function to copy the set
    # set2 = set1.copy()
    #
    # # prints the copied set
    # print(set2)

Student = {"name": "Ankit", "age": 21, "sex": "Male",
           "college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing keys details
print('The frozen set is:', key)


# creates a set
myset = set()
myset.add("D")
myset.add("F")
myset.add("t")
myset.add("S")
myset = sorted(myset)
for i in myset:
    print(i)

myset2 = myset.copy()

# for i1 in myset2:
#     print(i1)

S = {"ram", "rahim", "ajay", "rishav", "aakash"}
S = sorted(S)

# Print the set before using pop() method
# First element after printing the set will be popped out
print(S)

# Popping three elements and printing them
print(S.pop())
print(S.pop())
print(S.pop())

# The updated set
print("Updated set is", S)


