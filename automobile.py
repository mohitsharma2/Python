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
df=pd.read_csv("C:/Users/mohit/Desktop/FORSKCODE/Automobile.csv")
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


