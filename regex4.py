"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
  Output:    yogendra_54@forsk.com

    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]
"""

import re
mail=input("Enter email addresses:")
rx=re.search("[a-zA-Z0-9_-]+@[a-z]+\.[a-z]{3}",mail)
if rx!=None:
    print("Valid")
else:
    print("Invalid")
       
    

import re
list1=[]
for i in range(3):
    list1.append(input('enter email:'))
print(sorted(re.findall('^[a-z0-9_-]+@[a-z]+\.com',' '.join(list1))))


"""
output===================================================================


enter email:yogendra_54@forsk.com

enter email:ajeet@forsk.com

enter email:kunal-23@forsk.com
['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com']
"""