class college():
    
    def __init__(self,name,estabilshed_year,owner):
        self.name=name
        self.estabilshed_year=estabilshed_year
        self.owner=owner
        
class faculty(college):
    def __init__(self,firstname,lastname,sex,age,department,name,estabilshed_year,owner):
        college.__init__(self,name,estabilshed_year,owner)
        self.firstname=firstname
        self.lastname=lastname
        self.sex=sex
        self.age=age
        self.department=department
        
class student(college):
    def __init__(self,first_name,last_name,age,sex,section,name,estabilshed_year,owner):
        college.__init__(self,name,estabilshed_year,owner)
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.age=age
        self.section=section
        
c1=college('GIT',1967,'Sharma ji')
c2=college('JEC',1999,'Gupta ji')

f1=faculty('Mohit','Sharma','Male',26,'EE','GIT',1967,'Sharma ji')
f2=faculty('Yogendra','Yogi','Male',23,'CSE','JEC',1999,'Gupta ji')

s1=student('Kammo','Mishra','Female',22,'CSE','GIT',1967,'Sharma ji')
s2=student('Rajesh','Sharma','Male',25,'ECE','JEC',1999,'Gupta ji')

s1.section
s2.owner
        