a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operator (+, -, *, /): ")
if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    if(b==0):
        print("division by zero not possible")
    else:
        print(a/b)
else:
    print("Invalid operator. Run program again")