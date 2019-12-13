"""
Code Challenge
Name: 
    Pattern Builder
Filename: 
    pattern.py
Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
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
    5
Sample Output:
    Below is the output of execution of this program.
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
"""
'''
n=int(input('Enter no of rows'))
for i in range(1,n+1):
    for j in range(i-1):
        print('\u2605',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n-i):
        print('\u2605',end=' ')
    print()
'''

n=int(input('Enter no of rows'))
for i in range(1,n+1):
    if i<(n/2)+1:
        print(' \u2605'*i)
    else:
        print(' \u2605'*(n+1-i))
        

output:-------------------------------------------------------------------------

Enter no of rows9
 ★
 ★ ★
 ★ ★ ★
 ★ ★ ★ ★
 ★ ★ ★ ★ ★
 ★ ★ ★ ★
 ★ ★ ★
 ★ ★
 ★
