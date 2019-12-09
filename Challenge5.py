
'''
Challenge 5
Limit the number of guesses to maximum 6 tries
'''



        
import random
count=0
while count<6: 
    a = random.randrange(1,10)
    count+=1
    num = int(input("enter the Guess number:"))
    
    if a==num:
        print("number is {}, player wins and computer lose".format(num))
        break

    else:
        print("number is {}, player lose and computer wins".format(a))





'''
output--------------------------------------------------------------------------
enter the Guess number:5
number is 3, player lose and computer wins
enter the Guess number:6
number is 7, player lose and computer wins
enter the Guess number:6
number is 5, player lose and computer wins
enter the Guess number:5
number is 2, player lose and computer wins
enter the Guess number:5
number is 7, player lose and computer wins
enter the Guess number:5
number is 2, player lose and computer wins
'''
