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
import mysql.connector
import pandas as pd
connect_to_database=mysql.connector.connect(user='mohit121', password='iamroyal',host='db4free.net', database = 'bid_info')

create_cursor=connect_to_database.cursor()

create_cursor.execute(""" CREATE TABLE about_bid (
        Bid_no TEXT,
        item TEXT,
        Quantity_Required INTEGER,
        Department_Name_And_Address TEXT,
        Start_Date TEXT,
        End_Date TEXT
)"""
    )


connect_to_database.commit()

df= pd.read_csv('C:/Users/mohit/Desktop/Python/bid101_plus.csv')

print(df)

df.to_sql('bid_info',connect_to_database, if_exists='replace',index=False) # to store in data base
 # to store in data base
create_cursor.execute("SELECT * FROM about_bid")



 



















