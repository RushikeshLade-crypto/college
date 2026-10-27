#program to display first n multiples of a number
num = int(input("Enter the number: "))
n = int(input("Enter how many multiples (n): "))
print(f"\nThe first {n} multiples of {num} are:")

for i in range(1,n+1):
    multiple = n*i
    print(f"{num} x {i} = {multiple}")