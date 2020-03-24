# program to calculate and print roots of a quadratic equcation : ax^2 + bx + c=0 (a!=0)


import math

print("for quadratic equcation : ax^2 + bx + c=0,enter cofficient below:")

a=int(input("Enter a:")) 
b=int(input("Enter b:"))
c=int(input("Enter c:"))

if a==0:
    print("Value of 'a' should not be zero.")
    print("\n Aborting !!!")

else:
    value = b*b - 4 * a * c
    if value>0:
        root1=(-b+math.sqrt(value))/(2*a)
        root2=(-b-math.sqrt(value))/(2*a)
        
        print("Roots are real and unequal")
        print("Root1=",root1,"Root2=",root2)
        
    elif value==0:
        root1= -b/(2*a) 
        print("Roots are real and Equal")
        print("Root1=",root1,"Root2=",root1)
        
    else:
         print("Roots are Complex and Imaginary")

"""    
output===>        
        
Enter a:3

Enter b:5

Enter c:2
Roots are real and unequal
Root1= -0.6666666666666666 Root2= -1.0

"""        