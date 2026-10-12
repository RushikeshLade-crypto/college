# program to find roots of quadratic equation
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation")
else:
    D = b**2 - 4*a*c

    if D > 0:
        r1 = (-b + math.sqrt(D)) / (2*a)
        r2 = (-b - math.sqrt(D)) / (2*a)
        print("Roots are", r1, "and", r2)

    elif D == 0:
        r = -b / (2*a)
        print("Equal roots are", r)

    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*abs(a))

        print(f"Roots are {real} + {imag}i and {real} - {imag}i")