'''
Challenge 2
 Print the secret number and guess number when Player loses using format function 






n=int(input('Guess the number'))
import random
from random import randint
m=random.randint(1,10)
print('Secret number is:',m)
if n==m:
    print('Secret number is {} player wins and computer lose'.format(m))
else:
    print('Secret number is {} player lose and computer wins'.format(m))


output:-------------------------------------------------------------------------

Guess the number5
Secret number is: 7
Secret number is 7 player lose and computer wins
'''
