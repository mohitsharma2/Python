
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""


from selenium import webdriver
from collections import OrderedDict
import pandas as pd


url="https://bidplus.gem.gov.in/bidlists"

browser= webdriver.Chrome("E:\Driver\chromedriver.exe")

browser.get(url)


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for f in range(5):
      


    bid_table=browser.find_elements_by_class_name('border')
    
    for row in bid_table:
        block1=row.find_elements_by_tag_name('span')
        A= browser.find_elements_by_partial_link_text('GEM/')
        B.append(block1[0].text.strip())
        C.append(block1[1].text.strip())
        D.append(block1[2].text.strip())
        E.append(block1[3].text.strip())
        block2=row.find_element_by_class_name('add-height')
        F.append(block2.text.strip())
    for ji in A:
        G.append(ji.text)
    browser.find_element_by_xpath('//*[@id="pagination"]/ul/li/ul/li[5]/a').click()
col_name=['BID NO','Item','Quantity Required','Department Name And Address','Start Date','End Date']

df=pd.DataFrame(OrderedDict(zip(col_name,[G,B,C,F,D,E])))

df.to_csv('bid101_plus.csv')

browser.quit()