
"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your working diretory with the same
name as the image name.

Do not hardcode the name of the image

"""

import requests
r=requests.get('http://forsk.in/images/Forsk_logo_bw.png')

with open('forsk_logo_bw.png','wb') as f:
    f.write(r.content)


output====================================



C:/Users/mohit/forsk_logo_bw.png
