H = int(input("Enter hours: "))
M = int(input("Enter minutes: "))
S = int(input("Enter seconds: "))
Hs = H*60*60
Ms = M*60
totals = S+Hs+Ms
radian = totals/43200
degree = radian*360
print(f"angle is {degree} degree ")
