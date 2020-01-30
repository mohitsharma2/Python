"""
Code Challenge

Download the image from the URL and store in a file

https://imgs.xkcd.com/comics/python.png

"""



import requests
comics=requests.get("https://imgs.xkcd.com/comics/python.png")
with open("C:/Users/mohit/Desktop/python.png",'wb') as com:
    com.write(comics.content)




