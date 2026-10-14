'''A timestamp is three numbers: a number of hours, minutes and seconds. Given two
timestamps, calculate how many seconds is between them. The moment of the first
timestamp occurred before the moment of the second timestamp'''

h1 = int(input("Enter timestamp 1 hours: "))
m1 = int(input("Enter timestamp 1 minutes: "))
s1 = int(input("Enter timestamp 1 seconds: "))
h2 = int(input("Enter timestamp 2 hours: "))
m2 = int(input("Enter timestamp 2 minutes: "))
s2 = int(input("Enter timestamp 2 seconds: "))
if 0>h1 or h1>24 or 0>m1 or m1>60 or 0>s1 or s1>60 or 0>h2 or h2>24 or 0>m2 or m2>60 or 0>s2 or s2>60:
    print("Incorrect timestamp.")
else:
    d = abs((h1*60*60+m1*60+s1)-(h2*60*60+m2*60+s2))
    print("there are ",d," seconds between two timestamps")