"""
Code Challenge
  Name: 
    Regular Expression 3
  Filename: 
    regex3.py
  Problem Statement:
    You and Virat are good friends. 
    Yesterday, Virat received credit cards from ABCD Bank. 
    He wants to verify whether his credit card numbers are valid or not. 
    You happen to be great at regex so he is asking for your help!

    A valid credit card from ABCD Bank has the following characteristics:

    It must start with a '4', '5' or ' 6'.
    It must contain exactly 16 digits
    It must only consist of digits (0-9)
    It may have digits in groups of 4, separated by one hyphen "-"
    It must NOT use any other separator like ', ' , '_', etc
    It must NOT have 4 or more consecutive repeated digits 
 
  Hint: 
    Using Regular Expression 
  Input:
    4123456789123456
    5123-4567-8912-3456
    61234-567-8912-3456
    4123356789123456
    5133-3367 -8912-3456
    5123 - 3567 - 8912 - 3456
  Output:
    Valid
    Valid
    Invalid
    Valid
    Invalid
    Invalid
"""
i=0
import re
while(i<6):
    credit=input("Enter credit card number:")
    i+=1
    rx=re.search("(^[456])\d{3}[-]?\d{4}[-]?\d{4}[-]?\d{4}",credit)
    if rx!=None:
        print('Valid')
    else:
        print('Invalid')

        
"""
output==================================================================


Enter credit card number:4123456789123456
Valid
Enter credit card number:5123-4567-8912-3456
Valid
Enter credit card number:61234-567-8912-3456
Invalid
Enter credit card number:4123356789123456
Valid
Enter credit card number:5133-3367 -8912-3456
Invalid
Enter credit card number:5123 - 3567 - 8912 - 3456
Invalid
"""
