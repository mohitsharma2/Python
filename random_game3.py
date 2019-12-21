"""
Name: 
    Random Game 3         
Filename:
    randon_game3.py
Problem Statement:
    Write a program for a Higher / Lower guessing game
    The computer randomly generates a sequence of up to 10 numbers
    between 1 and 13. The player each after seeing each number
    in turn has to decide whether the next number is higher or lower.
    If you can remember Brucie’s ‘Play your cards right’ it’s basically
    that. If you get 10 guesses right you win the game.
    Starting number : 12
    Higher(H) or lower(L)? L
    Next number 8
    Higher(H) or lower(L)? L
    Next number 11
    You lose
Data:
    Not required
Extension:
    Give the players two lives
    Make sure only H or L can
    be entered  
Hint: 
    Use a condition controlled loop (do until, while etc) to control the
    game. Do not find yourself repeating the same code over and over!
    You don't need to remember all 10 numbers just the current number
    /next number. Don’t forget you’ll have to keep a count of the
    number of turns they’ve had. 
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
i=1
s=0
while(i<=10):
    n1=random.randint(1,13)
    print('comp_num',n1)
    inp=input('Enter your guess "H" or "L" ')
    n2=random.randint(1,13)
    print(n2)
    if inp.upper()=="H":
        i+=1
        if n1<=n2:
            s=s+1
            print('Right guess')
        else:
            print('wrong guess')
    elif inp.upper()=='L':
        i+=1
        if n1>=n2:
            print('Right guess')
            s=s+1
        else:
            print('wrong guess')
    else:
        print('Invalid input')
if s>=10:
    print('you win')
else:
    print('you loss')
































