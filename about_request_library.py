import requests
channel="https://api.thingspeak.com/update?api_key=WN7NO9WD8GC4JN63&field1=10&field2=573&field3=403"
rs=requests.get(channel)


read="https://api.thingspeak.com/channels/974679/feeds.json?api_key=W2HE4S4JP4RJRLJZ&results=2"
response = requests.get(read)

ro=response.json()

