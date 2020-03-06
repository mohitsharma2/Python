"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
        
        
https://bigml.com/user/francisco/gallery/dataset/5163ad540c0b5e5b22000383
https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas       
https://github.com/guipsamora/pandas_exercises/
        
        
"""

import pandas as pd

df=pd.read_csv("C:/Users/mohit/Desktop/FORSKCODE/Telecom_churn.csv")
df.head()
print(df.shape)
print(df.columns)
print(df.info())

#We can change the column type with the astype method. Let's apply this method to the Churn feature to convert it into int64:
df["churn"]=df["churn"].astype('int64')

df.describe()

df.describe(include=['object', 'bool'])

df['churn'].value_counts()

df['churn'].value_counts(normalize=True)

df.sort_values(by='total day charge',ascending=True).head()

df.sort_values(by=['churn', 'total day charge'],ascending=[True, False]).head()

df['churn'].mean()


df[df["churn"]==1].mean()

df[df["churn"]==1]['total day minutes'].mean()

df.loc[0:5,'state':'area code']

df.iloc[0:5,0:4]   # 0:4 means first 4 column 

df[-1:]

df.apply(np.max)

df[df['state'].apply(lambda state: state[1] == 'V')].head()
df[df['state'].apply(lambda state: state[0] == 'W')].head()

columns_to_show = ['total day minutes', 'total eve minutes', 
                   'total night minutes']

df.groupby(['churn'])[columns_to_show].describe(percentiles=[])



























