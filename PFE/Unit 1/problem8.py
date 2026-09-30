import math

a = int(input("Enter students in class 1: "))
b = int(input("Enter students in class 2: "))
c = int(input("Enter students in class 3: "))

desk1= math.ceil(a/2)
desk2= math.ceil(b/2)
desk3= math.ceil(c/2)

total_desk = desk1+desk2+desk3

print(f"{total_desk} minimum desks required")