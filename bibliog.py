               
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
class Book():
    def __init__(self,authorfirst_name, authorlast_name,book_title, place, publisher, year):
        self.authorfirst_name = authorfirst_name
        self.authorlast_name = authorlast_name
        self.book_title = book_title
        self.place = place
        self.publisher = publisher
        self.year = year
        
    def write_bib_entry(self):
#        return ', '.join([self.authorfirst_name,self.authorlast_name,self.book_title,self.place,self.publisher,str(self.year)])
        return self.authorfirst_name \
               + '  ' + self.authorlast_name \
               + ', ' + self.book_title + ', ' + self.place \
               + ',' + self.publisher + ', ' \
               + str(self.year) + '.'
               
#        print('Author name:',self.authorfirst_name,self.authorlast_name)
#        print('Title of Book:',self.book_title)
#        print('Place:',self.place)
#        print('Publisher :',self.publisher )
#        print('Year:',self.year)

    
    def make_authoryear(self):
        self.author_year=self.authorlast_name+'('+str(self.year)+')'

beauty=Book('mohit','sharma','you are the password of my life','MP','RRK','2019')

pynut=Book('puneet','kumar','Hum Char','Rajasthan','SKS','2018')



print(pynut.authorfirst_name,pynut.authorlast_name)


print(pynut.write_bib_entry())

beauty.year=2010
print(beauty.year)

make_up=Book('Anthony','Doerr','All the Light We Cannot See','UK','MPE','2014')
print(make_up.write_bib_entry())

beauty.make_authoryear()
print(beauty.author_year)


class Article():
    def __init__(self, authorfirst_name, authorlast_name,book_title, place, publisher, year,volume,pages):
        self.authorfirst_name = authorfirst_name
        self.authorlast_name = authorlast_name
        self.book_title = book_title
        self.place = place
        self.publisher = publisher
        self.year = year
        self.volume=volume
        self.pages=pages
        
    def write_bib_entry(self):
#        return ', '.join([self.authorfirst_name,self.authorlast_name,self.book_title,self.place,self.publisher,str(self.year),\
#                          str(self.volume),str(self.pages)])
        return self.authorfirst_name \
               + '  ' + self.authorlast_name \
               + ', ' + self.book_title + ', ' + self.place \
               + ',' + self.publisher + ', ' \
               + str(self.year) \
               + str(self.volume)\
               +str(self.pages) + '.'

    def make_authoryear(self):
        self.authoryear=self.authorlast_name+'('+str(self.year)+')'





