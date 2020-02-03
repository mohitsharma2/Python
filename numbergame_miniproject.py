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

"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""

"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""

while(True):
    

    import random
    secret_number=random.randint(1,10)
    guess_number=int(input("Enter the Guess number:"))
    
    if guess_number==secret_number:
        print("Congratulation You WIN and Computer loose")
        break
    else:
        print("I'am sorry! You Loose and Computer Wins.Your Guess_number is:{} and secret_number is:{}".format(guess_number,secret_number))
    if guess_number<secret_number:
        print("Too Low")
    else:
        print("Too High")
    print("Play again")

    
output======================================================

Enter the Guess number:5
I'am sorry! You Loose and Computer Wins.Your Guess_number is:5 and secret_number is:3
Too High
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:2
Too High
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:7
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:3
Too High
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:8
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:10
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:6
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:6
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:2
Too High
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:7
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:2
Too High
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:5
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:5
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:7
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:8
Too Low
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:1
Too High
Play again

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:6
Too Low
Play again

Enter the Guess number:6
I'am sorry! You Loose and Computer Wins.Your Guess_number is:6 and secret_number is:5
Too High
Play again

Enter the Guess number:4
Congratulation You WIN and Computer loose