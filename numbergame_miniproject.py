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
"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""


"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""


"""
Challenge 6
    Print the number of tries left 
"""

"""
Challenge 7
    Lets give user the option to play again
"""

"""
Challenge 8
    Catch when someone submits a non integer
"""


n=1
while(n<7):
    
    import random
    x=input("Do you want to play then press '1':")
    if x=="1":
        print(x)
    else:
        break
    secret_number=random.randint(1,10)
    try:
        guess_number=int(input("Enter the Guess number:"))
    except:
        print("Invalid input! Int value only ")
    n+=1
    if guess_number==secret_number:
        print("Congratulation You WIN and Computer loose")
        break
    else:
        print("I'am sorry! You Loose and Computer Wins.Your Guess_number is:{} and secret_number is:{}".format(guess_number,secret_number))
    if guess_number<secret_number:
        print("Too Low")
    else:
        print("Too High")
    
     
    
    print("Number of Tries Left:",7-n)
    
output====================================================================================    

Enter the Guess number:6
I'am sorry! You Loose and Computer Wins.Your Guess_number is:6 and secret_number is:7
Too Low
Play again
Number of Tries Left: 5

Enter the Guess number:5
I'am sorry! You Loose and Computer Wins.Your Guess_number is:5 and secret_number is:10
Too Low
Play again
Number of Tries Left: 4

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:10
Too Low
Play again
Number of Tries Left: 3

Enter the Guess number:7
I'am sorry! You Loose and Computer Wins.Your Guess_number is:7 and secret_number is:6
Too High
Play again
Number of Tries Left: 2

Enter the Guess number:5
I'am sorry! You Loose and Computer Wins.Your Guess_number is:5 and secret_number is:3
Too High
Play again
Number of Tries Left: 1

Enter the Guess number:4
I'am sorry! You Loose and Computer Wins.Your Guess_number is:4 and secret_number is:3
Too High
Play again
Number of Tries Left: 0