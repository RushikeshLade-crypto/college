a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Send 1 for addition for numbers\nSend 2 for substraction\nSend 3 for multiplication\nSend 4 for division: "))
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
else:
    print(a/b)