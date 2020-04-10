# program to input a number and test if it is a prime number.
    

number=int(input("Enter number:"))
lim=int(number/2)+1
for i in range(2,lim):
    rem=number%i
    if rem==0:   
        print(number,"is not a prime number")
        break
else:
    print(number,"is a prime number")
            
"""   
output===>

Enter number:4545
4545 is not a prime number

"""