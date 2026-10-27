#program to display first n multiples of a number
n = int(input("Enter a number: "))
m = int(input("Enter value of n: "))
m2 = (n*m)+1
for i in range (n,m2,n):
    print(i)