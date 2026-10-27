#program to calculate sum and average of n numbers
n = int(input("Enter a number: "))
if n<= 0:
    print("Please enter a positive number.")
else:
    total_sum = 0

    for i in range(1,n+1):
        total_sum += i

    average = total_sum/n
    print(f"Sum = {total_sum}\nAverage = {average}")