#Program to display first n Fibonacci numbers
n = int(input("Enter the number of terms (n): "))
if n<=0:
    print("Enter a positive integer greater than 0")
else:
    print(f"The first {n} Fibonacci numbers are: ")
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        next_num = a+b
        a = b
        b = next_num

    print()