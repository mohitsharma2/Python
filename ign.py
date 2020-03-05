"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
        
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/mohit/Desktop/Python/ign.csv")
print(df)
df.columns


#   Let's say we want to find games released for the Xbox One 
#   that have a score of more than 7.

find_game=df[(df['platform']=='Xbox 360') & (df['score']>7)]
print(find_game)

find_game.head(10)


#   review distribution for the Xbox One vs the review distribution 
#   for the PlayStation 4.We can do this via a histogram, which will plot the 
#   frequencies for different score ranges.


x=df[df['platform']=='PlayStation 4']



y=df[(df['platform']=='Xbox 360')]

plt.hist(x['score'],bins=[0,2,4,6,8,10],width=0.5)
plt.xlabel('PlayStation 4')
plt.ylabel('score')

plt.hist(y['score'],bins=[0,2,4,6,8,10])
plt.xlabel('Xbox 360')
plt.ylabel('score')

