
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

import pymongo
from pymongo import MongoClient
import pandas as pd

cluster = MongoClient("mongodb+srv://mohit121:iamroyal@cluster0-zkejb.mongodb.net/test?retryWrites=true&w=majority")
mydb=cluster.mohit
bid=mydb.bid

df= pd.read_csv('C:/Users/mohit/Desktop/Python/bid101_plus.csv')

records_ = df.to_dict(orient = 'records')
result = mydb.bid.insert_many(records_ )

