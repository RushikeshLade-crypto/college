# a consumer consumes 250 units at 8Rs per unit. Calculate the bill, 100-unit blocks and remaining units.

units = 250
rate = 8
bill = units*rate
block = units//100
remaining = units%100

print("Bill = ",bill)
print("100-unit Blocks = ",block)
print("Remaining unit = ",remaining)