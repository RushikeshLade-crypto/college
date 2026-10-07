# program to find roots of quadratic equation
a = int(input("Enter the coefficient of x square: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))
discriminant = b*b - 4*a*c
if discriminant > 0:
    rootd = discriminant**0.5
    root1 = (-1*b+rootd)/2*a
    root2 = (-1*b-rootd)/2*a
    print(f"roots of the equation are {root1} & {root2}")
elif discriminant < 0:
    print("roots of this equation are not real")
else:
    rootd = discriminant**0.5
    root1 = (-1*b+rootd)/2*a
    root2 = (-1*b-rootd)/2*a
    print(f"roots of the equation are {root1} & {root2}")    