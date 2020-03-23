"""
Program that inputs three numbers and calculates two sums as per this:
    
    sum1 as the sum of all input numbers
    
    sum2 as the sum of non-dublicate numbers; if there are dublicates numbers in the input, 
    ignores them
    
eg: Input of numbers 2,3,4 will give two sums as 9 and 9
    Input of numbers 3,2,3 will give two sums as 8 and 2 (both 3 is ignored for second sum)
    Input of numbers 4,4,4 will give two sums as 12 and 0 (all 4 ignored for second sum) 
"""
#1.

num1=int(input("Enter first number:"))

num2=int(input("Enter second number:"))

num3=int(input("Enter third number:"))  

sum1=num1+num2+num3
print("Sum of all input numbers:",sum1)

sum2=0

if num1 != num2 and num1 != num3:
    sum2+=num1

if num2 != num1 and num2 != num3:
    sum2+=num2

if num3 != num1 and num3 != num2:
    sum2+=num3

print("sum of non-dublicate numbers",sum2)
    
#2.

num1=int(input("Enter first number:"))

num2=int(input("Enter second number:"))

num3=int(input("Enter third number:"))  

sum1=num1+num2+num3
print("Sum of all input numbers:",sum1)

sum2=0

if num1==num2:
    if num3!=num1:
        sum2+=num3
else: #(num1!=num2)
    if num1==num3:
        sum2+=num2
        
    else:
        if num2==num3:
            sum2+=num1
            
        else:
            sum2+=num1+num2+num3
    
print("sum of non-dublicate numbers",sum2)
  
"""
output===>

Enter second number:2

Enter third number:3
Sum of all input numbers: 8
sum of non-dublicate numbers 2
"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    