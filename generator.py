"""
Name: 
    generator       
Filename:
    generator.py 
Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers. 
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
    2, 4, 7, 8, 9, 12
Sample Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '12')
""" 



'''

tuple1=list1=input('Enter the numbers: ').split(',')
list2=list(list1)
tuple2=tuple(tuple1)
print('List: ',list2)
print('Tuple: ',tuple2)


output====================================================================


Enter the numbers: 2,4,7,8,9,12
List:  ['2', '4', '7', '8', '9', '12']
Tuple:  ('2', '4', '7', '8', '9', '12')

'''
