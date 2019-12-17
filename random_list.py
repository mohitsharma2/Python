
"""
Name: 
    2 Dimensional Random List         
Filename:
    random_list.py
Problem Statement:
    Create a 2-Dimensional list of list of integers 10 by 10.
    Fill the 2-Dimensional list with random numbers in the range 0 to 255
    Display the array on the screen showing the numbers
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
    Not Available 
Sample Output:
    Not Available 
"""
'''
import random
list1=[]
list2=[]
for i in range(10):
    list1=[]
    for j in range(10):
        list1.append(random.randrange(0,255))
    list2.append(list1)
for i in list2:
    print(i)


output=========================================================================

[132, 104, 6, 20, 43, 145, 98, 154, 32, 91]
[167, 122, 45, 164, 16, 236, 141, 185, 212, 254]
[184, 38, 82, 89, 132, 128, 215, 10, 158, 77]
[198, 172, 207, 113, 21, 19, 79, 123, 229, 50]
[110, 146, 86, 49, 21, 252, 245, 179, 221, 6]
[140, 211, 191, 64, 197, 230, 10, 161, 107, 39]
[83, 10, 249, 251, 75, 53, 97, 157, 121, 215]
[79, 231, 116, 222, 222, 152, 68, 160, 250, 70]
[28, 254, 88, 180, 33, 160, 90, 227, 191, 228]
[76, 162, 75, 52, 158, 25, 141, 247, 44, 200]
'''

'''
import random
list1 = []
list2 = []

for item in range(10):
    for index in range(10):
        list1.append(random.randint(0,255))
    list2.append(list1.copy())
    list1.clear()
print(list2)

output=======================================================================

[[250, 4, 162, 2, 89, 94, 181, 157, 177, 62], [28, 242, 22, 223, 211, 246, 30, 0, 205, 52], [43, 124, 8, 58, 205, 45, 121, 81, 36, 91], [240, 14, 131, 53, 49, 35, 173, 54, 195, 239], [149, 224, 226, 139, 13, 187, 10, 41, 174, 83], [20, 205, 154, 30, 155, 185, 124, 16, 49, 80], [205, 241, 74, 40, 13, 167, 194, 77, 139, 102], [124, 142, 49, 205, 82, 32, 69, 23, 2, 40], [54, 155, 51, 36, 97, 154, 192, 33, 213, 127], [41, 194, 188, 206, 31, 30, 148, 119, 45, 90]]

'''
