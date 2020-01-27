
"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing in human readable format
"""

import requests
import time
city=input("Enter City Name: ")

url1= "http://api.openweathermap.org/data/2.5/weather" 
url2 = "?q="+city
url3 = "&appid=79fe4df01f6b5fb98ea704285bd3026b" 
url=url1+url2+url3
x=requests.get(url)
y=x.json()
print(y)
y["coord"]
y["weather"]
y['wind']
time.ctime(y['sys']['sunrise'])
time.ctime(y['sys']['sunset'])

output========================================================

Enter City Name: Jaipur
{'coord': {'lon': 75.82, 'lat': 26.92}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 290.15, 'feels_like': 287.4, 'temp_min': 290.15, 'temp_max': 290.15, 'pressure': 1021, 'humidity': 36}, 'visibility': 2000, 'wind': {'speed': 1.5}, 'clouds': {'all': 0}, 'dt': 1578642975, 'sys': {'type': 1, 'id': 9170, 'country': 'IN', 'sunrise': 1578620826, 'sunset': 1578658816}, 'timezone': 19800, 'id': 1269515, 'name': 'Jaipur', 'cod': 200}
y["coord"]
 {'lon': 75.82, 'lat': 26.92}
 
 y["weather"]
 [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}]

y['wind']
 {'speed': 1.5}
 
 time.ctime(y['sys']['sunrise'])
'Fri Jan 10 07:17:06 2020'

time.ctime(y['sys']['sunset'])
'Fri Jan 10 17:50:16 2020'