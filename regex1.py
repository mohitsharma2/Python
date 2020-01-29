"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
p=0
while(p<4):
    import re
    s=input("Enter the number:")
    p+=1
    aba=re.search("([+-]*)\d+\.\d+",s)
    if aba!=None:
        print(True)
    else:
        print(False)

output=========================================================


Enter the number:4
False
Enter the number:4.000
True
Enter the number:-1.00
True
Enter the number:+4.54
True
