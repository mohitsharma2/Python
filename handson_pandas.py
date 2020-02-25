"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""

import pandas as pd

df = pd.read_csv("C:/Users/mohit/Desktop/FORSKCODE/Salaries.csv")

#1. Which Male and Female Professor has the highest and the lowest salaries

x=df[(df['rank']=='Prof') & (df['sex']=='Male')]
print(x)
maximum = x[x['salary']== x['salary'].max()]
print(maximum)

minimum = x[x['salary']== x['salary'].min()]
print(minimum)

x=df[(df['rank']=='Prof') & (df['sex']=='Male')]
print(x)
maximum = x[x['salary']== x['salary'].max()]
print(maximum)

minimum = x[x['salary']== x['salary'].min()]
print(minimum)


y=df[(df['rank']=='Prof') & (df['sex']=='Female')]
print(y)
maximum = y[y['salary']== y['salary'].max()]
print(maximum)

minimum = y[y['salary']== y['salary'].min()]
print(minimum)

#2. Which Professor takes the highest and lowest salaries.


high=df[df['rank']=='Prof']
high['salary'].max()

low=df[df['rank']=='Prof']
low['salary'].min()

#3. Missing Salaries - should be mean of the matching salaries of those whose service is the same

df1=df[df['salary'].isnull()]['service']

df[(df['service']==18) | (df['service']==2)]

df2=df[df['service']==18]
a=df2['salary'].mean()    # service 18 ki salries ka mean nikal kr nanm dalna h.
                          # service 2 ki salries ka mean nikal kr nanm dalna h.
df3=df[df['service']==2]
b=df3['salary'].mean()

df[df['service']==18]['salary'].fillna(a)
df[df['service']==2]['salary'].fillna(b)




