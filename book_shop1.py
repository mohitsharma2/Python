
"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint:
    Write a Python program using lambda and map.
    
# Assume the data in form of list of list
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

"""



orders = [ ["34587", "Learning Python", "Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python", "Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python", "Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3", "Bernd Klein",  3, 24.99]]

order_number=list(map(lambda x:x[0],orders))
print(order_number)

Book_Title=list(map(lambda x:x[1],orders))
print(Book_Title)

author=list(map(lambda x:x[2],orders))
print(author)

quantity=list(map(lambda x:x[3],orders))
print(quantity)
Price_per_Item=list(map(lambda x:x[4],orders))
print(Price_per_Item)

a=zip(order_number,Book_Title,author,Price_per_Item)
print(list(a))
list1=[]
for i in orders:
    list1.append(i[0])
    list1.append(i[-1]*i[-2])
print(list1)
list1=list(map(lambda x:(x[0],x[-1]*x[-2]),orders))
print(list1)

list2=list(map(lambda x:x[-1]*x[-2]+10 if x[-1]*x[-2]<100 else x[-1]*x[-2],orders))
print(list2)

output=====================================================================


['34587', '98762', '77226', '88112']
['Learning Python', 'Programming Python', 'Head First Python', 'Einführung in Python3']
['Mark Lutz', 'Mark Lutz', 'Paul Barry', 'Bernd Klein']
[4, 5, 3, 3]
[40.95, 56.8, 32.95, 24.99]
[('34587', 'Learning Python', 'Mark Lutz', 40.95), ('98762', 'Programming Python', 'Mark Lutz', 56.8), ('77226', 'Head First Python', 'Paul Barry', 32.95), ('88112', 'Einführung in Python3', 'Bernd Klein', 24.99)]
['34587', 163.8, '98762', 284.0, '77226', 98.85000000000001, '88112', 74.97]
[('34587', 163.8), ('98762', 284.0), ('77226', 98.85000000000001), ('88112', 74.97)]
[163.8, 284.0, 108.85000000000001, 84.97]
