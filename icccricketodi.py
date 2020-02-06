
"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import requests
odi=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text    
print(odi)
match=BeautifulSoup(odi)

#match.table
# or
tables=match.find_all('table')
right_table=match.find('table',class_='table')
print(right_table)

A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) !=0:
   # or
    #if len(cells)==5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
    
from collections import OrderedDict
col_name=['Pos','Team','Weighted Matches','Points','Rating']
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
print(col_data)
import pandas as pd
df=pd.DataFrame(col_data)
df.to_csv("odi.csv")

