# Program to display numbers in the reverse order
number = int(input("Enter an integer: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
    print(digit,reverse,number)

print("Number in reverse order:", reverse)