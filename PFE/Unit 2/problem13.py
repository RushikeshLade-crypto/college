#program to check if a year is leap
year = int(input("Enter year: "))
if year%4==0:
    print(year," is leap year")
else:
    print(year," is not leap year")