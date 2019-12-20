"""
Name: 
    Sentence       
Filename:
    Sentence.py
Problem Statement:
    You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code. 
    The sentence you want to encode is the lazy dog jumped over the quick brown 
    fox and the output should be ’vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz’ 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Create a dictionary mapping each letter to its number in the alphabet
    Create a dictionary mapping each number to its letter in the alphabet
    Go through each letter in the sentence and find the corresponding number, add 2 and then find the new corresponding letter
    Make sure to take care of the edge cases so that if you get the letter z, it maps to b… ect
    Print the encoded string  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
"""

list1='abcdefghijklmnopqrstuvwxyzab'
dict1={}
t=2
for i in list1[:-2]:
    dict1[i]=list1[t]
    t=t+1
print(dict1)

str1='the lazy dog jumped over the quick brown fox'
str2=''
for i in str1:
    if i!=' ':
        str2=str2+dict1[i]
    else:
        str2=str2+i
print(str2)

'''

output=====================================================================

vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz
'''
