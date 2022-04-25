
# if ...else and elif block execution
A = int(input(" enter no A "))
B = int(input(" enter no B "))
print(A, ",", B, "are 2 nos")
if (A > 0) and (B > 0):
    print(A, ",", B, "are 2 positive nos")
    if (A > B) :
        print(A," is a largest no ==> IF PART")
        print(B, "is a smallest no ==> IF PART")
    else :
        print(B," is a largest no ==> INNER ELSE PART");
        print(A, "is a smallest no ==> INNER ELSE PART");
elif (A > 0):
    print(A, " is a largest no ==> ELIF PART")
    print(A, " is a positive no ==> ELIF PART")
else:
    print(B, " is a largest no ==> OUTER ELSE PART")
    print(B, " is a positive no ==> OUTER ELSE PART")

