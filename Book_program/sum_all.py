# program to calculate and print the sums of even and odd integers of the first "n" natural numbers.

n=int(input("Enter a number at which you want sum: "))

number=1
sum_of_even=sum_of_odd=0

while number<=n:
    
    if number%2==0:
        sum_of_even+=number
    
    else:
       sum_of_odd+=number
      
    number+=1
    
print("Sum of even integers is :",sum_of_even)
print("Sum of odd integers is :",sum_of_odd)

"""

output===>

Enter a number at which you want sum: 50
Sum of even integers is : 650
Sum of odd integers is : 625

"""