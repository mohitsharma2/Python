
"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a int
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
"""

import pandas as pd
import numpy as np


df=pd.read_csv("C:/Users/mohit/Desktop/python/Baltimore_City_Employee_Salaries_FY2014.csv")
df.columns

#  1.assign it as a int
x=df["AnnualSalary"]

"""
0    11310.0
1    53428.0
2    68300.0
3    62000.0
4    43999.0
Name: AnnualSalary, dtype: float64

"""
x.head()

x=df["AnnualSalary"].astype("int64")

x.describe

x.head()

"""
0    11310
1    53428
2    68300
3    62000
4    43999
Name: AnnualSalary, dtype: int64

"""

#2. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
#       Sort the data and display to show who get the highest salary

read=df.groupby(['JobTitle','AnnualSalary'])
read.count()