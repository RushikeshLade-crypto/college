#program to display first n numbers
n = int(input("enter the number: "))
start = 0
while True:

    if n > start:
        start += 1
        print(start)

    else:
        break