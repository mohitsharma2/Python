'''
# Problem Statement:
    Write a program that asks the user, again and again, to enter a number.
    When the user enters an empty string, then stop asking for additional inputs.
    Along the way, as the user is entering numbers, 
    I want you to store those numbers in a list. 
    I also want you to keep track of the minimum and maximum values that you've seen so far.
    When the user has finished entering numbers, your program should print out:
         The sum of these numbers
         The average (mean) of these numbers
         The largest and smallest numbers you received from the user





import statistics
list1=[]
while(1):
    inp=input('Enter a number')
    if inp.isdigit():
        list1.append(int(inp))
    else:
        break
print(sum(list1))
print(statistics.mean(list1))

sum=0
for i in list1:
    sum=sum+i
print(sum/len(list1))    
print(max(list1))
print(min(list1))


output:--------------------------------------------------------------------------


Enter a number15
Enter a number25
Enter a number10
Enter a number20
Enter a numberk
70
17.5
17.5
25
10
'''


