"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.
"""

import random
secret_number=random.randint(1,10)
guess_number=int(input("Enter the Guess number:"))

if guess_number==secret_number:
    print("Congratulation You WIN and Computer loose")
else:
    print("I'am sorry! You Loose and Computer Wins.Your Guess_number is:{} and secret_number is:{}".format(guess_number,secret_number))
if guess_number<secret_number:
    print("Too Low")
else:
    print("Too High")
    
output======================================================

Enter the Guess number:5
I'am sorry! You Loose and Computer Wins.Your Guess_number is:5 and secret_number is:3
Too High