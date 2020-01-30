
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

"""and"""

import requests
import time
city=input("Enter the city name:")



url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c6085dce47fe2425cc9893f2f8e22f3c"
a=requests.get(url)
or

a=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c6085dce47fe2425cc9893f2f8e22f3c")



b=a.json()
print(b)
b['coord']
b['weather']
b['wind']['speed']
time.ctime(b['sys']['sunrise'])
time.ctime(b['sys']['sunset'])





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

"""and"""


{'coord': {'lon': 76, 'lat': 29},
 'weather': [{'id': 800,
   'main': 'Clear',
   'description': 'clear sky',
   'icon': '01n'}],
 'base': 'model',
 'main': {'temp': 284.76,
  'feels_like': 282.76,
  'temp_min': 284.76,
  'temp_max': 284.76,
  'pressure': 1018,
  'humidity': 65,
  'sea_level': 1018,
  'grnd_level': 993},
 'wind': {'speed': 1.33, 'deg': 6},
 'clouds': {'all': 0},
 'dt': 1580316122,
 'sys': {'country': 'IN', 'sunrise': 1580262398, 'sunset': 1580301066},
 'timezone': 19800,
 'id': 1270260,
 'name': 'Haryana',
 'cod': 200}

b['coord']
Out[53]: {'lon': 76, 'lat': 29}

b['weather']
Out[54]: [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]

b['wind']['speed']
Out[55]: 1.33

time.ctime(b['sys']['sunrise'])
Out[56]: 'Wed Jan 29 07:16:38 2020'

time.ctime(b['sys']['sunset'])
Out[57]: 'Wed Jan 29 18:01:06 2020'

