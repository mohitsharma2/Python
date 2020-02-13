"""
Code Challenge
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]

"""

list1 = [7, 13, 17, 231, 12, 8, 3]
iter1=iter(list1)
l=len(list1)
def running_avg():
    summ=0
    i=1
    
    while i<=l:
        summ+=next(iter1)
        yield summ/i  
        i+=1
f1=running_avg()   
next(f1)


"""
output============================================================

Out[323]: 7.0

next(f1)
Out[324]: 10.0

next(f1)
Out[325]: 12.333333333333334

next(f1)
Out[326]: 67.0

next(f1)
Out[327]: 56.0

next(f1)
Out[328]: 48.0

next(f1)
Out[329]: 41.57142857142857

next(f1)
Traceback (most recent call last):

  File "<ipython-input-330-3f8d8c50d063>", line 1, in <module>
    next(f1)

StopIteration  
"""        







