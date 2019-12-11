"""
Challenge 8
    Catch when someone submits a non integer
"""


while(1):
    n=input('Enter the Guess number: ')
    if n.isdigit()==False:
        print('Please enter interger value: ')
        continue
    else:
        print()
        
    import random
    from random import randint
    a=random.randint(1,10)
    print('Random number is:',a)
    if n==a:
        print('player wins and computer lose')
        break
    else:
        print('player lose and computer wins')



