"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""


names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print(names)


names = ['Mary', 'Isla', 'Sam']
output=list(map(lambda x:hash(x),names))
print(output)


output============================================================

[-5303544729643217079, 2171107064266216918, 846935377990551478]
[-5303544729643217079, 2171107064266216918, 846935377990551478]
