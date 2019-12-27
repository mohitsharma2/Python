
"""
Name: 
    Playing Cards         
Filename:
    Playing_Cards.py
Problem Statement:
    Write a program that will generate a random playing card 
    e.g. ‘9 Hearts’, ‘Queen Spades’ when the return key is pressed.
    Rather than generate a random number from 1 to 52. 
    Create two random numbers – one for the suit and one for the card.
    However we don't want the same card drawn twice.
Data:
    Not required
Extension:
    Update this program by using an list to prevent the same card being dealt 
    twice from the pack of cards.
    
    Convert this code into a procedure ‘DealCard’ that will display the card dealt or ‘no more cards’.
    Call your procedure 53 times! 
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
list1=['Spades','Club','Diamond','Heart']
list2=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
list3=[]
t=0
k='a'
while(t<52):
    i=random.choice(list1)
    j=random.choice(list2)
    if i+j in list3:
        print('Card is taken',i+j)
    else:
        print('You got your card',i+j)
        list3.append(i+j)
    c=input('Enter "c" to choose another card:')
    if c!='c':
        break
    else:
        t+=1
        
        
            

