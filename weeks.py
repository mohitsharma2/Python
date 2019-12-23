"""
Name: 
    weeks       
Filename:
    weeks.py 
Problem Statement:
    Write a program that adds missing days to existing tuple of days 
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
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
Sample Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
""" 


week1=('Monday', 'Wednesday', 'Thursday', 'Saturday')
week2=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
week1 = tuple(set(week1).union(set(week2)))
print(week1)

output====================================================================================


('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
