"""
Name: 
    Unlucky 13         
Filename:
    unlucky.py
Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user
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
    13, 1, 2, 13, 2, 1, 13 
Sample Output:
    3 
"""

list1=input('Enter numbers').replace(' ','').split(',')
list2=[]
list3=[]
for i in range(len(list1)):
    if list1[i]=='13':
        list2.append(i)
        list2.append(i+1)

for i in range(len(list1)):
    if i not in list2:
        list3.append(int(list1[i]))
print(sum(list3))


        





