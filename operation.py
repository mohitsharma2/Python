"""
Name: 
    Operations Function         
Filename:
    operation.py
Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)
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
    5,2,6,2,3
Sample Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]
"""


list1=input('Enter the number:').split(',')
def add(list1):
    j=0
    for i in list1:
        j=j+int(i)
    print('sum: ',j)
add(list1)


def multiply(list1):
    j=1
    for i in list1:
        j=j*int(i)
    print('Multiply',j)
multiply(list1)


def largest(list1):
    for i in range(len(list1)-1):
        a=list1[i]
        b=list1[i+1]
        if a<b:
            pass
        else:
            list1[i+1]=list1[i]
            list1[i]=b
    print('Largest: ',list1[-1])
largest(list1)


def smallest(list1):
    for i in range(len(list1)-1):
        a=list1[i]
        b=list1[i+1]
        if a<b:
            pass
        else:
            list1[i+1]=list1[i]
            list1[i]=b
    print('Smallest:',list1[0])
smallest(list1)

def sort(list1):
    for i in range(len(list1)-1):
        a=list1[i]
        b=list1[i+1]
        if a<b:
            pass
        else:
            list1[i+1]=list1[i]
            list1[i]=b
    print('sorted:',list1)
sort(list1)

def without_duplicates(list1):
    list1=set(list1)
    list1=list(list1)
    print('without_duplicates',list1)
without_duplicates(list1)


output===============================================================


Enter the number:5,2,6,2,3
sum:  18
Multiply 360
Largest:  6
Smallest: 2
sorted: ['2', '2', '3', '5', '6']
without_duplicates ['3', '6', '2', '5']




