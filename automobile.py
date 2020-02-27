"""
Code Challenge
  Name: 
    Automobile Analysis
  Filename: 
    automobile.py
  Problem Statement:
    (Automobile.csv)
    Read the Automobile.csv file and perform the following task :
    1. Handle the missing values for Price column
    2. Get the values from Price column into a numpy.ndarray
    3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

# 1. Handle the missing values for Price column

import pandas as pd
df=pd.read_csv("C:/Users/mohit/Desktop/python/Automobile.csv")
df.columns

No_price=df[df["price"].isnull()]
print(No_price)

No_price.fillna(0)

# 2. Get the values from Price column into a numpy.ndarray

import numpy as np
price=np.array(df["price"])
print(type(price))
print (price.dtype)
print (price.ndim)
print (price.shape)
print (price.itemsize)
print(price.size)   #  no of item
print (price.nbytes)
print (price.strides)   

# 3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price

x=df["price"]
x.min()
x.max()
x.mean()
x.std()
df["price"].agg(['min','max','mean','std'])


"""
output=================================================================

     symboling  normalized_losses     make  ... city_mpg highway_mpg price
9            0                NaN     audi  ...       16          22   NaN
44           1                NaN    isuzu  ...       38          43   NaN
45           0                NaN    isuzu  ...       38          43   NaN
129          1                NaN  porsche  ...       17          28   NaN

[4 rows x 26 columns]


     symboling  normalized_losses     make  ... city_mpg highway_mpg price
9            0                0.0     audi  ...       16          22   0.0
44           1                0.0    isuzu  ...       38          43   0.0
45           0                0.0    isuzu  ...       38          43   0.0
129          1                0.0  porsche  ...       17          28   0.0

[4 rows x 26 columns]


<class 'numpy.ndarray'>
float64
1
(205,)
8
205
1640
(8,)

min      5118.000000
max     45400.000000
mean    13207.129353
std      7947.066342
Name: price, dtype: float64

"""