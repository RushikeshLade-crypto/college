# program to find maximum of three numbers
#method 3 using and & or operator
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
greator = (n1>=n2 and n1>=n3 and n1) or (n2>=n3 and n2>=n1 and n2) or n3
print(greator)