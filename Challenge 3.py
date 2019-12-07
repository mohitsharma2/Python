
'''
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif.








n=int(input('Guess the number'))
import random
from random import randint
m=random.randint(1,10)
print(m)
if n==m:
    print('player wins and computer lose')
elif n>m:
     print('too HIGH')
elif n<m:
    print('too low')
else:
     print('player lose and computer wins')


output--------------------------------------------------------------------------

Guess the number5
2
too HIGH
'''
