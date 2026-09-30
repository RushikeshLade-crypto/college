Name = "Rushikesh Balaji Lade"
College = "VIT, Pune"
Branch = "Computer Engineering"
Div = "H"
Roll = 803
sub1 = int(input("Enter marks of first subject: "))
sub2 = int(input("Enter marks of second subject: "))
sub3 = int(input("Enter marks of third subject: "))
sub4 = int(input("Enter marks of fourth subject: "))
sub5 = int(input("Enter marks of fifth subject: "))
total = sub1+sub2+sub3+sub4+sub5
percent = total/5
a = percent
if(a<33):
    grade = "fail"
elif(a<60):
    grade = "C"
elif(a<80):
    grade = "B"
elif(a<90):
    grade = "A"
else:
    grade = "A+"
print(f"Name of the student is {Name}\nStudying {Branch} in {College}\nDivision: {Div}\nRoll No.: {Roll}\nPercentage: {percent}\nGrade: {grade}")