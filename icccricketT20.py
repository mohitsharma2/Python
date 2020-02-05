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
t20=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/t20i").text
print(t20)
match=BeautifulSoup(t20)
print(match)
t20_table=match.find('table',class_='table')
print(t20_table)

A=[]
B=[]
C=[]
D=[]
E=[]

for row in t20_table.findAll('tr'):
    column=row.findAll('td')
    if len(column)!=0:   #if len(column)==5:
        A.append(column[0].text.strip())
        B.append(column[1].text.strip())
        C.append(column[2].text.strip())
        D.append(column[3].text.strip())
        E.append(column[4].text.strip())
        
        
from collections import OrderedDict        
        
title=['Pos','Team','Weighted Matches','Points','Rating']      
title_data=OrderedDict(zip(title,[A,B,C,D,E]))
print(title_data)

import pandas as pd

df=pd.DataFrame(title_data)        
df.to_csv("t20.csv")
        
        
        
        