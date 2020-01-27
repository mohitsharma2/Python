"""
Code Challenge

Download the image from the URL and store in a file

https://imgs.xkcd.com/comics/python.png

"""



import requests
a=requests.get("https://imgs.xkcd.com/comics/python.png")

with open('comics','wb') as f:
    f.write(a.content)


output===================================




file:///C:/Users/mohit/comics

