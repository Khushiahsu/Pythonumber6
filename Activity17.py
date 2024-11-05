#Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?

a = int(input("Enter Aaravs mark"))
b = int(input("Enter Aaravs mark"))
c = int(input("Enter Aaravs mark"))
d = int(input("Enter Aaravs mark"))
e = int(input("Enter Aaravs mark"))
sum = a+b+c+d+e
average = sum/5


if average>=91 and average<=100:
    print("Your grade is A1")

elif average>=81 and average<=90:
    print("Your grade is A2")
elif average>=71 and average<=80:
    print("Your grade is B1")
elif average>=61 and average<=70:
    print("Your grade is B2")
elif average>=51 and average<=60:
    print("Your grade is C1")
elif average>=41 and average<=50:
       print("Your grade is C2")
elif average>=31 and average<=40:
    print("Your grade is D1")
elif average>=21 and average<=30:
    print("Your grade is D2")
elif average>=11 and average<=20:
    print("Your grade is E1")
elif average>=0 and average<=11:
    print("Your grade is E2")
else:
    print('invalid input')

