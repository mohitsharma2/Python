               
"""
Code Challenge
  Filename:
      bibliog.py
      
    1. Create a two instances of Book in the name of beauty and pynut
    2. How would you print out the author attribute of the pynut instance
    3. If you type print beauty.write_bib_entry() at the interpreter, what will happen?
    4. How would you change the publication year for the beauty book to"2010"?
    5. Create another instance of the Book class as makeup, book of your choice
       Execute the write_bib_entry method for that
    6. Add a method make_authoryear to the class definition that will create
       an attribute authoryear and will set that attribute to a string that
       has the last name of the author and then the year in parenthesis.
       The method should not have a return statement.
    7. Create an Article class that manages information about articles. 
       It will be very similar to the class definition for Book, except publisher
       and place information will be unneeded and article title, volume number,
       and pages will be needed. Make sure this class also has the methods
       write bib entry and make authoryear.
          
"""

class Book:
    
    def __init__(self,firstname,lastname,booktitle,bookvolumenumber,bookpages,publication_year):
        self.firstname=firstname
        self.lastname=lastname
        self.booktitle=booktitle
        self.bookvolumenumber=bookvolumenumber
        self.bookpages=bookpages
        self.publication_year=publication_year
        
    def write_bib_entry(self):
#        return ', '.join([self.firstname+self.lastname,self.booktitle,str(self.bookpages),str(self.publication_year)])
        return self.firstname \
               + '  ' + self.lastname \
               + ', ' + self.booktitle + ', ' + self.bookvolumenumber \
               + ',' + self.bookpages + ', ' \
               + self.publication_year + '.'
               
#        print('Author name:',self.firstname,self.lastname)
#        print('Title of Book:',self.booktitle)
#        print('Volume Number:',self.bookvolumenumber)
#        print('Number of Pages in Book:',self.bookpages)
#        print('Publication Year:',self.publication_year)
#        
    def make_authoryear(self):
        return self.firstname \
               + '  ' + self.lastname \
               + ', ' + self.booktitle + ', ' + self.bookvolumenumber \
               + ',' + self.bookpages + ', ' \
               + self.publication_year + '.'
        

        

        
        
beauty=Book('mohit','sharma','you are the password of my life','12','366','2019')

pynut=Book('puneet','kumar','Hum Char','9','264','2018')
 #beauty and pynut are instance
makeup=Book('Anthony','Doerr','All the Light We Cannot See','1','544','2014')


print(write_bib_entry(beauty))

print(write_bib_entry(pynut))
    
beauty.publication_year=2010

print(write_bib_entry(beauty))

print(write_bib_entry(makeup))




"""
output=========================================================================

mohit  sharma, you are the password of my life, 12,  366, 2019.

puneet  kumar, Hum Char, 9:  264, 2018.

Anthony  Doerr, All the Light We Cannot See, 1,  544, 2014.

#after modification in publication year

mohit  sharma, you are the password of my life, 12,  366, 2010.

"""