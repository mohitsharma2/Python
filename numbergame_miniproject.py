import random
secret_number=random.randint(1,10)
guess_number=int(input("Enter the Guess number:"))

if guess_number==secret_number:
    print("Congratulation You WIN and Computer loose")
else:
    print("I'am sorry! You Loose and Computer Wins")
