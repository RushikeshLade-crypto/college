#program to calculate factorial of a number, module method
import math

num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exists for negative numbers")
else:
    print(f"the factorial of {num} is {math.factorial(num)}")