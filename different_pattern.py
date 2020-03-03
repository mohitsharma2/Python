
for i in range(5):             #it decide the rows
    for j in range(5):      #it decide the column
        print("*",end=" ")# Iterate those numbers using outer for loop to handle the number of rows.
#Inner loop to handle the number of columns.
#Inner loop iteration depends on the values of the outer loop.
    print() #new line
    print("\n")
"""    
output===============================

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""

for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

"""    
output=================================================

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 

"""

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

"""
output===============================================

1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
"""

for i in range(5):
    for j in range(65,65+4):
        print(chr(j),end=" ")
    print()    

for i in range(5):
    for j in range(65+i):
        print(j)
    print()







