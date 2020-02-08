'''
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
'''

from selenium import webdriver

url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

browser= webdriver.Chrome("E:\Driver\chromedriver.exe")

browser.get(url)

code=browser.find_element_by_tag_name('tbody')

A=[]
B=[]
C=[]
D=[]
E=[]


for row in code.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        

from collections import OrderedDict

col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 

print(df)

df.to_csv("icccricket_odi_selenium.csv")

browser.quit()
