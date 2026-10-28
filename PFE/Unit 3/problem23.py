#Program to check if a number is prime
num = int(input("Enter a number: "))
r1 = num%2
r2 = num%3
r3 = num%5
r4 = num%7
r5 = num%11
if num==1:
    print("One is not composite nor prime number")
elif r1==0 or r2==0 or r3==0 or r4==0 or r5==0:
    print(num," is composite number")
else:
    print(num," is prime number")