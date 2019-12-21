
"""
Name: 
    Centered Average         
Filename:
    centered.py
Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is the 
    mean average of the values, except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. Use int division to produce the final average. 
    You may assume that the array is length 3 or more.
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
    1, 2, 3, 4, 100 
Sample Output:
    3 
"""
t=0
list1=[]
inp=input('Enter the numbers: ').split(',')
for i in inp:
    list1.append(int(i))
list1=sorted(list1)
for i in list1[1:len(list1)-1]:
    t=t+int(i)
print(t/(len(list1)-2))  
print(list1)

'''
output===========================================================================================

Enter the numbers: 1,2,3,4,100
3.0
[1, 2, 3, 4, 100]
'''
