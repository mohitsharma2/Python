"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
      
"""
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("C:/Users/mohit/Desktop/python/training_titanic.csv")

df.columns

df1=df['Survived'].value_counts()
print(df1)

df1.value_counts(normalize = True)*100


#graph
plt.title("Titanic Alive-Death Ratio")
labels=["Survived","Not Survived"]
sizes=[342,549]
colors = ['brown', 'olive']
explode = (0.05, 0)  # explode 1st slice  0.5 means 50% of curve radius

plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.3f%%',shadow=True,startangle=60)
plt.axis("equal")
plt.show()



#df2=df[(df['Sex']=='male') & (df['Survived']==1)]
#df2['Survived'].value_counts()

#df3=df[(df['Sex']=='male') & (df['Survived']==0)]
#df3['Survived'].value_counts()

#or

df2=df[(df['Sex']=='male')]
df2['Survived'].value_counts()

df2['Survived'].value_counts(normalize = True)*100


#graph
plt.title("Male")
labels="Survived","Not Survived"
sizes=[18.89,81.11]
colors = ['gold','lightcoral']
explode = (0, 0)  # explode 1st slice  0.5 means 50% of curve radius

plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.2f%%',shadow=True,startangle=180)
plt.axis("equal")
plt.show()

#df4=df[(df['Sex']=='female') & (df['Survived']==1)]
#df4['Survived'].value_counts()
#df5=df[(df['Sex']=='female') & (df['Survived']==0)]
#df5['Survived'].value_counts()


df4=df[(df['Sex']=='female')]
df4['Survived'].value_counts()
df4['Survived'].value_counts(normalize = True)*100



#graph
plt.title("Female")
labels="Survived","Not Survived"
sizes=[74.20,25.79]
colors = ['purple', 'cyan']
explode = (0.3, 0)  # explode 1st slice  0.5 means 50% of curve radius

plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.2f%%',shadow=True)
plt.axis("equal")
plt.show()


dd=df.groupby("Age")[['Survived']]
dd.count()



child1=df[(df["Age"]<=18) & (df['Survived']==1)]
dd=child1.groupby("Age")[['Survived']]
print("Child(0-18) which is survived:", dd.count().sum())

child2=df[(df["Age"]<=18) & (df['Survived']==0)]
dd=child2.groupby("Age")[['Survived']]
print("Child(0-18) which is not survived:", dd.count().sum())

#graph
plt.title("Child")
labels="Survived","Not Survived"
sizes=[70,69]
colors = ['yellow','red']
explode = (0, 0)  # explode 1st slice  0.5 means 50% of curve radius

plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.2f%%',shadow=True,startangle=90)
plt.axis("equal")
plt.show()

#or

child1=df[(df["Age"]<=18)]
child1['Survived'].value_counts(normalize = True)*100

# create child column


df['Child']=df['Age'].map(lambda x: 1 if x<=18 else 0)
df['Child'].value_counts(normalize = True)*100


#graph
plt.title("Adult-Child Graph")
labels="Above 18 year","Below 18 year"
sizes=[84.39,15.60]
colors = ['olive','brown']
explode = (0.1, 0)  # explode 1st slice  0.5 means 50% of curve radius

plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.2f%%',shadow=True)
plt.axis("equal")
plt.show()


