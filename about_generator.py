
# A Python program to generate squares from 1 to 1000 using yield and therefore generator 

# An infinite generator function that prints next square number. It starts with 1 

def nextSquare(): 
	i = 1; 

    # An Infinite loop to generate squares 
	while True: 
		yield i*i				 
		i += 1 # Next execution resumes from this point	 

# Driver code to test above generator function 

for num in nextSquare(): 
	if num > 1000: 
		break	
	print(num) 

output===========================================================

1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
441
484
529
576
625
676
729
784
841
900
961


# to generate first "n" number
     
def  firstn(num):
    n=1
    while n<=num:
        yield n
        n+=1
        
for x in firstn(10):
    print(x)
    
output======================================================

1
2
3
4
5
6
7
8
9
10
    
    
    