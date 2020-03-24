#program that reads the three number and prints them in acsending order.

a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))

if a<b and a<c:
    if b<c:
        print("Acsending order is:",a,b,c)
        print("Line number:",1)
    else:
        print("Acsending order is:",a,c,b)
        print("Line number:",2)
        
elif b<a and b<c:
    if a<c:
        print("Acsending order is:",b,a,c)
        print("Line number:",3)
    else:
        print("Acsending order is:",b,c,a)
        print("Line number:",4)
else:
    if c<a and c<b:
        if a<b:
            print("Acsending order is:",c,a,b)
            print("Line number:",5)
        else:
            print("Acsending order is:",c,b,a)
            print("Line number:",6)

"""
output===>

Enter the first number:40

Enter the second number:21

Enter the third number:98
Acsending order is: 21.0 40.0 98.0
Line number: 3    

"""

