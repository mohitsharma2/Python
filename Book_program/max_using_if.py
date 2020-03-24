# Program to accept three integers and print the largest of the three.Make use of only if statement. 

x=float(input("Enter First number:"))
y=float(input("Enter Second number:"))
z=float(input("Enter Third number:"))

max=x
if y>max:
    max=y

if z >max:
    max=z

print("Largest number is:",max)

"""
output===>

Enter First number:12

Enter Second number:54

Enter Third number:45
Largest number is: 54.0
"""