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
call=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/test").text
test=BeautifulSoup(call)

match=test.find('table',class_='table')
print(match)

A=[]
B=[]
C=[]
D=[]
E=[]

for row in match.find_all("tr"):
    column=row.find_all('td')
    if len(column)!=0:
        A.append(column[0].text.strip())
        B.append(column[1].text.strip())
        C.append(column[2].text.strip())
        D.append(column[3].text.strip())
        E.append(column[4].text.strip())

from collections import OrderedDict
title=['Pos','Team','Weighted Matches','Points','Ranking']

title_name=OrderedDict(zip(title,[A,B,C,D,E]))
print(title_name)

import pandas as pd

df=pd.DataFrame(title_name)
df.to_csv("test.csv")
