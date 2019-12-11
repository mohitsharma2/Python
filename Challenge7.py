'''
Challenge 7
    Lets give user the option to play again
'''




while(1):
    
    n=int(input('Enter the Guess number: '))
    import random
    from random import randint
    a=random.randint(1,10)
    print("random number is: ",a)
    if a==n:
        print('player wins and computer lose')
        break
    else:
        print('player lose and computer wins')
        m= input("Do you want to play again then press 1,otherwise press any key")

        if m=="1":
            print()
        else:
            break

'''
output--------------------------------------------------------------------------

Enter the Guess number: 8
random number is:  3
player lose and computer wins
Do you want to play again then press 1,otherwise press any keyp
'''
