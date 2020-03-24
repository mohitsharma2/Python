#program that reads the three number and prints them in acsending order.

a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))

if a<b and a<c:
    if b<c:
        print(a,b,c)
        print("Line number:",1)
    else:
        print(a,c,b)
        print("Line number:",2)
        
elif b<a and b<c:
    if a<c:
        print(b,a,c)
        print("Line number:",3)
    else:
        print(b,c,a)
        print("Line number:",4)
else:
    if c<a and c<b:
        if a<b:
            print(c,a,b)
            print("Line number:",5)
        else:
            print(c,b,a)
            print("Line number:",6)
    