"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
j=0
list1=[]
import re
while(j<3):

    s=input("Enter email addresses:")
    j+=1
    a=re.findall("[a-zA-Z0-9-_]+@[a-zA-Z]+\.com",s)
    
    for i in a:
        list1.append(i)
    m=sorted(list1)
    print(m)

s=input("Enter email addresses:")
a=re.search("[a-zA-Z0-9-_]+@[a-zA-Z]+\.com",s)
if a!=None:
    print("valid")
else:
    print("no")

import re
list1=[]
for i in range(3):
    list1.append(input('enter email:'))
print(sorted(re.findall('[a-z0-9_-]+@[a-z]+\.com',' '.join(list1))))

output==================================================

enter email:brian-23@hackerrank.com

enter email:lara@hackerrank.com

enter email:britts_54@hackerrank.com
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']





















