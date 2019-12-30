"""
Name: 
    Bricks         
Filename:
    bricks.py
Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
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
    2, 2, 11
Sample Output:
    True
""" 

x=input('Enter small bircks:')

y=input('Enter big brick:')

z=input('Enter target lenght:')

if (int(x)+int(y)*5)>=int(z):
    print('True ! target can be made')
else:
    print('False ! sortage of bricks')

output====================================================================

Enter small bircks:2
Enter big brick:2
Enter target lenght:11
True ! target can be made
