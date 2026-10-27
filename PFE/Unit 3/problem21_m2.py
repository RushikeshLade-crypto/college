#program to calculate factorial of a number
n = int(input("Enter a number: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    factorial = 1
    for i in range (1, n+1):
        factorial *= i
        print(factorial)