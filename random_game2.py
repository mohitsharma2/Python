"""
Name: 
    Random Game 2         
Filename:
    randon_game2.py
Problem Statement:
    Write a program for a game where the computer generates a
    random starting number between 20 and 30.
    The player and the computer can remove 1,2 or 3 from the number
    in turns. Something like this...
    Starting number : 25
    How many do you want to remove? 3
    22 left
    Computer removes 2
    20 left
    The player who has to remove the last value to bring the number
    down to 0 is the loser.
    1 left
    Computer removes 1
    You win!
    Easy option
    Get the computer to choose a number between 1—3 at random
    Harder option
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
""" 



import random
number=random.randint(20,31)
print('you got ',number,' to play')



while(number>0):
    comp_num=random.randint(1,3)
    print('computer gets',comp_num)
    number= number-comp_num
    print('you get number',number)
    if number<=0:
        print('you lost')
        break
    user_number=input('Enter the number 1,2 or 3 ')
    number= number-int(user_number)
    if number<=0:
        print('you win ')
        break

output===============================================================

you got  28  to play
computer gets 3
you get number 25
Enter the number 1,2 or 3 3
computer gets 2
you get number 20
Enter the number 1,2 or 3 3
computer gets 1
you get number 16
Enter the number 1,2 or 3 3
computer gets 2
you get number 11
Enter the number 1,2 or 3 3
computer gets 2
you get number 6
Enter the number 1,2 or 3 3
computer gets 1
you get number 2
Enter the number 1,2 or 3 2
you win 
