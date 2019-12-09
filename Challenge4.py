
'''
Challenge 4
    Let people play again and again until he guesses the right secret number
'''



while True:
    import random

    a = random.randint(1,10)

    num = int(input("enter the Guess number:"))

    if a==num:
        print("number is {}, player wins and computer lose".format(num))
        break

    else:
        print("number is {}, player lose and computer wins".format(a))



'''
output--------------------------------------------------------------------------


enter the Guess number:5
number is 6, player lose and computer wins
enter the Guess number:9
number is 9, player wins and computer lose
'''
