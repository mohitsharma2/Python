
"""
Name: 
    Treasure Hunt Game         
Filename:
    treasure.py
Problem Statement:
    Create a simple treasure hunt game.
    Create a list of list of integers 10 by 10.
    In a random position in the array store the number 1.
    Get the user to enter coordinates where they think the treasure is.
    If there is a 1 at this position display ‘success’.
    Repeat Until they find the treasure
    Add a feature to say 'hot' 'cold' 'warm' depending on how close their guess 
    was to the actual hidden location.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
"""

import random
list1=[]
list2=[]
for i in range(10):
    list1=[]
    for j in range(10):
        list1.append(random.randrange(0,10))
    list2.append(list1)
for i in list2:
    print(i)
    
n=input('Enter the row:')
m=input('enter the col:')
if list2[int(n)][int(m)]==1:
    print('you win')
else:
    print('you lost')

  
