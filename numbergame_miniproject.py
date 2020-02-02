import random
secret_number=random.randint(1,10)
guess_number=int(input("Enter the Guess number:"))

if guess_number==secret_number:
    print("Congratulation You WIN and Computer loose")
else:
    print("I'am sorry! You Loose and Computer Wins.Your Guess_number is:{} and secret_number is:{}".format(guess_number,secret_number))

output======================================================

Enter the Guess number:6
I'am sorry! You Loose and Computer Wins.Your Guess_number is:6 and secret_number is:7
