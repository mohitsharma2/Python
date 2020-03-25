#find out index of duplicate number

list2=[]    
list1=[10,20,30,10,40,50,10,60,10]
for i in range(len(list1)) :
     if list1[i]==10:
         list2.append(i)
if len(list2)>1:
    print(list2[1:])
else:
    print('no duplicates ')

"""
output===>
[3, 6, 8]
"""