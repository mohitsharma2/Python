#program to find the multiles of a number(divisor) out of given five number. 

print("Enter the five number below")

num1=float(input("Enter first number:"))

num2=float(input("Enter second number:"))

num3=float(input("Enter third number:"))  

num4=float(input("Enter fourth number:"))  

num5=float(input("Enter fifth number:"))  

divisor=float(input("Enter divisor number:"))

count=0
remainder=num1 % divisor

if remainder ==0:
    print(num1)
    count+=1

remainder=num2 % divisor

if remainder ==0:
    print(num2)
    count+=1

remainder=num3 % divisor

if remainder ==0:
    print(num3)
    count+=1

remainder=num4 % divisor

if remainder ==0:
    print(num4)
    count+=1

remainder=num5 % divisor

if remainder ==0:
    print(num5)
    count+=1
print(count,"multiple of ",divisor,"found")
"""
output===>

Enter the five number below

Enter first number:10

Enter second number:5

Enter third number:15

Enter fourth number:20

Enter fifth number:26

Enter divisor number:5
10.0
5.0
15.0
20.0
4 multiple of  5.0 found
"""

































