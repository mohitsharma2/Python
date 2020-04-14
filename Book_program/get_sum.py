"""
program to input some numbers repeatedly and print their sum. 
The program ends when the user say "no" more to enter(normal termination )or program aborts when 
the number entered is less than zero.

"""
count=sum=0
ans='y'
while ans=="y" :
    num=int(input("Enter the number: "))
    if num<0:
        print(" The number entered is less than zero.Abort!!!")
        break
    sum+=num
    count+=1
    ans= input("Want to enter more numbers?(y/n)")
    
else:
    print("You entered",count,"numbers so far.")
    
print("Sum of numbers entered is",sum)
