"""
Name: 
    Pangram         
Filename:
    pangram.py
Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    The five boxing wizards jumps. 
    Sphinx of black quartz, judge my vow.
    The jay, pig, fox, zebra and my wolves quack!
    Pack my box with five dozen liquor jugs.
Sample Output:
    NOT PANGRAM 
    PANGRAM
    PANGRAM
    PANGRAM
"""
t=1
while(t<=4):
    t+=1
    inp=input('Enter the string: ').replace('.','').replace('!','').replace(' ','').replace(',','')
    inp=inp.lower()
    print(inp)
    str1='abcdefghijklmnopqrstuvwxyz'
    for i in str1:
        if i not in inp:
            print('NOT PANGRAM')
            break
        else:
            if i==str1[-1]:
                print('PANGRAM')
   # t=input('Enter "stop" to exit')           
'''
output=======================================================

Enter the string: The five boxing wizards jumps.
thefiveboxingwizardsjumps
NOT PANGRAM
Enter the string: Sphinx of black quartz, judge my vow.
sphinxofblackquartzjudgemyvow
PANGRAM
Enter the string: The jay, pig, fox, zebra and my wolves quack!
thejaypigfoxzebraandmywolvesquack
PANGRAM
Enter the string: Pack my box with five dozen liquor jugs.
packmyboxwithfivedozenliquorjugs
PANGRAM
''' 
