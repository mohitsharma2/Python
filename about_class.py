#normal function

class person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        
p1=person('Mohit','Sharma',26)

print("Full name:",p1.fname,p1.lname," and Age is:",p1.age)


#about inheritance 

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def hello(self):
        print("My name is:",self.fname,self.lname)
        
m1=person("Shyam","Gupta")
#Use the Person class to create an object, and then execute the hello method:

m1.hello()

#output==My name is: Shyam Gupta

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def hello(self):
        print("My name is:",self.fname,self.lname)

class student(person):
    pass

m1=student("Shyam","Gupta")

m1.hello()

#output==My name is: Shyam Gupta
           
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def hello(self):
        print("My name is :",self.fname,self.lname)
        
class student(person):
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

        












