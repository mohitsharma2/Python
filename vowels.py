"""
Name: 
    Vowels Finder
Filename: 
    vowels.py
Problem Statement:
    Remove all the vowels from the list of states  
Hint: 
    Use nested for loops and while
Data:
    Not required
Extension:
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""

list1=[]
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
for i in state_name:
    for j in i:
        if j in ['A','a','E','e','I','i','O','o','U','u']:
            i=i.replace(j,'')
    list1.append(i)
print(list1)


output==============================================================


['lbm', 'Clfrn', 'klhm', 'Flrd']
