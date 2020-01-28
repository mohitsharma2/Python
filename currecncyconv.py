"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245
    or
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""



import requests
rupees=float(input("Enter the amount in USD: "))
a="http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245"
s=requests.get(a)
y=s.json() #to convert json to dict
'''
k = list(y.values())
m = k[0]*rupees
print(m)
'''
n=y['USD_INR']*rupees
print('USD_INR is: ',n)


output==================================================

Enter the amount in USD: 100
USD_INR is:  7097.375
