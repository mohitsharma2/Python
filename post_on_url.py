"""
Research the below wesbite and post some data on it
https://requestbin.com
"""
import requests
posting="https://ens27inllwrg.x.pipedream.net"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(posting,data,headers)
    return response

print ( post_method().text )
