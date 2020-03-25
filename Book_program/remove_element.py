#WAP to remove all ‘Y’ present in list1=['priya','ram','yiot' ].

#method1

list2=[]
list1=['priya','ram','yiot']
for i in list1 :
    if "y" in i:
        list2.append(i.replace("y",""))
    else:
        list2.append(i)
print(list2)

#method 2

list1=['priya','ram','yiot']
for i in range(len(list1)) :
    if "y" in list1[i]:
        list1[i]=list1[i].replace("y","")
print(list1)

"""
output===>

['pria', 'ram', 'iot']
 
"""        
         
         
         
         
         
         
         

















