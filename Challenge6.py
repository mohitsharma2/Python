
'''
Challenge 6
    Print the number of tries left

'''


import random
count=0
while count<6:
    a= random.randint(1,10)
    count+=1
    num = int(input("enter the Guess number:"))
    if a==num:
        print("number is {}, player wins and computer lose".format(num))
        break

    else:
        print("number is {}, player lose and computer wins".format(a))
    
        print('your guess left: ',6-count)



'''
output--------------------------------------------------------------------------

enter the Guess number:7
number is 4, player lose and computer wins
your guess left:  5
enter the Guess number:7
number is 10, player lose and computer wins
your guess left:  4
enter the Guess number:8
number is 9, player lose and computer wins
your guess left:  3
enter the Guess number:7
number is 10, player lose and computer wins
your guess left:  2
enter the Guess number:7
number is 10, player lose and computer wins
your guess left:  1
enter the Guess number:8
number is 10, player lose and computer wins
your guess left:  0
'''
