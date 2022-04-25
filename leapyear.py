year = input("Enter year to check for leap year : ")
year = int(year)
if ((year % 4) == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

