class person():
    def __init__(self,name,wife,child): # create an instance/object (its a maker of objects) 
        self.name=name
        self.wife=wife      #"name,wife,child"  they are variables
        self.child=child

    def of_type(self): # self represents the objects so you can access all the 
                       # obejcts/instance variable in functions.
        if self.child >=3:
            print("Great stamina")
        else:
            print("Build stamina")
            
person1=person('mohit','ko',2)       #here mohit and yogendra is objects
person2=person('yogendra','janu',1)

print(person1.name)
print(person2.child)
person1.of_type()

#inheritance

class person():
    def __init__(self,height,weight,color): # create an instance/object (its a maker of objects) 
        self.height=height
        self.weight=weight
        self.color=color
        print('person conn')
    def of_type(self):
        print('person type')
        
    
class male(person):
    sex='male'
    
    def __init__(self,name,age,height,weight,color):
        person.__init__(self,height,weight,color)
        self.name=name
        self.age=age
        print('male constructor')
    def of_type(self):
        
        print('he type')
    
class female(person):
    def __init__(self,name,age,height,weight,color):
        person.__init__(self,height,weight,color)
        self.name=name
        self.age=age
        print('female con')
    def of_type(self):
        print('she type')
    
p1=person(6.0,68,'black')
m1=male('mohit',24,5.5,60,'fair')
f1=female('kohit',23,5.1,52,'fair')

print(f1.color)