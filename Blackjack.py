"""
Name: 
    Blackjack         
Filename:
    Blackjack.py
Problem Statement:
    Play a game that draws two random cards.
    The player then decides to draw or stick.
    If the score goes over 21 the player loses (goes ‘bust’).
    Keep drawing until the player sticks.
    After the player sticks draw two computer cards. 
    If the player beats the score they win. 
Data:
    Not required
Extension:
    Aces can be 1 or 11! The number used is whichever gets the highest score.  
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
input1=''
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
while(input1==''):
    a=random.choice(list1)
    b=random.choice(list1)
    if (a+b)>=21:
        print('you bust')
    else:
        c=random.choice(list1)
        d=random.choice(list1)
        if (a+b)>(c+d):
            print('You win')
            print('you have',a+b,'computer has',c+d)
        else:
            print('You loose')
            print('you have',a+b,'computer has',c+d)
    input1=input('Press "Enter" to continue:')

'''
output===========================================================


You loose
you have 7 computer has 16
Press "Enter" to continue:
you bust
Press "Enter" to continue:
You loose
you have 6 computer has 16
Press "Enter" to continue:
You loose
you have 19 computer has 22
Press "Enter" to continue:
you bust
Press "Enter" to continue:
You loose
you have 11 computer has 13
Press "Enter" to continue:
You win
you have 14 computer has 9
Press "Enter" to continue:h
'''
