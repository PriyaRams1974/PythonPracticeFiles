# numerator = 10
# denominator = 0
# print(numerator/denominator)
# ==========================

# try:
#     numerator = int(input("Enter numerator "))
#     denominator = int(input("Enter denominator "))
#     result = numerator/denominator
#     print(result)
# except:
#    print("Denominator cannot be zero")
# ================================
try:
    numerator = int(input("Enter numerator "))
    denominator = int(input("Enter denominator "))
    result = numerator/denominator
    print(result)

    mylist = [1, 2, 3]
    i = int(input("enter index: "))
    print(mylist[i])
except ZeroDivisionError:
   print("Denominator cannot be zero")
except IndexError:
   print("Index is out of range")
print("program ends")
# ======================


