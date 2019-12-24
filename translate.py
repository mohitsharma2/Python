"""
Name: 
    Translate Function         
Filename:
    translate.py
Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User
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
    This is fun
Sample Output:
    ToThohisos isos fofunon
"""

str1=''
inp=input('Enter the string: ')
conso='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
for i in inp:
    if i in conso:
        str1=str1+(i+'o'+i)
    else:
        str1=str1+i
        
print(str1)

output================================================================


Enter the string: This is fun
ToThohisos isos fofunon
