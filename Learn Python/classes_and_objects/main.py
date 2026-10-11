# creating a class

class Student:
    # A constructor is used to initialize an object's attributes.
    def __init__(self,name,age,field,school):
        self.name = name
        self.age =age
        self.field=field
        self.school=school
    def introduce(self):
        print(f'I am {self.name} and am {self.age} years old pursuing PhD in {self.field} at {self.school}')    


# Creating objects from a class (a blueprint).
student_1 = Student('John Doe',29,'Computer Science','MIT')   
student_2 = Student('David',21,'Maths and Computer science','Caltech')
student_1.introduce()     
student_2.introduce()

# attributes  
  # Instance attributes are variables that are unique to each object and are set with the __init__ method.
  # Class attributes are variables that are common to all objects of the same class.

class Cars :
    company = 'Tesla'
    print(company)

    def __init__(self,model,plate_number):
        self.model =model
        self.plate_number=plate_number

    def describe(self):  #methods
        print(f'This car is {self.model} with plate number {self.plate_number} it was created by {self.company}')    


car_1 = Cars('Model 3','RAE 123A') 
car_2 = Cars('Model Y','RAB 456B')   
car_3 = Cars('Cybertruck','RAC 789C')    


print(car_1.company,car_2.company,car_3.company) # tesla * 3 bcz company is the same for all cars
print(car_1.model,car_2.model,car_3.model) # unique

# Methods are functions defined in a class. See line 30.

car_1.describe()
car_2.describe()
car_3.describe()


# Special methods are also known as magic methods or dunder methods.

print (3 .__add__(4))   # same as print(3+4) or print((3).__add__(4))  
# Note the space after 3; otherwise, Python will interpret it as if you were writing a float number.

print("Hello world".__len__())  # 11

# Think of special methods as directing interactions between a programmer and the Python language interpreter.
# When you write print(3+4), Python handles the addition behind the scenes, as if you wrote print(3 .__add__(4)).

# When we create our Python classes, we can customize these methods to do what we want.
# Python doesn't know how to use them with our classes as it does with its own data types. Consider the following example.


class Book:
    def __init__(self,book_name,book_pages):
        self.name = book_name
        self.pages = book_pages

book1 = Book("Think Python",244)   
book2 = Book("Introduction to Information Retrieval",581) 
print(len(book1.name))   # here you specify what you directly want it will work 

# But what if you want len() to return the number of pages?

#  print(len(book1))  This will return TypeError: object of type 'Book' has no len() 
# to fix it

class Mountain:
    def __init__(self,mountain_name,mountain_height):
        self.name = mountain_name
        self.height = mountain_height

    def __len__(self):
        return self.height   

mountain1 = Mountain("Mount Everest",8849)  
print(len(mountain1),"metres")   # prints 8846 metres

# look in the file fccCartExample.py for advanced example


# Working with object attributes dynamically.

# This is achieved using the built-in functions getattr(), setattr(), hasattr(), and delattr().

class Shoes:
    def __init__(self,brand,name):
        self.brand =brand
        self.name = name

shoes1 = Shoes("Nike","Nike Pegasus")    
print(getattr(shoes1,'name'))   # Nike Pegasus
print(getattr(shoes1,"price","$2500")) # $2500 is the default value it will be printed bcz there is no attibute price in shoes1

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))   # You can use to interact with user inputs easily 

# Listing Attributes With dir()

class Game:
    def __init__(self,name,players,referees):
        self.name = name
        self.players = players
        self.referees = referees

    def playing(self):
        print(self.name,"is being played")    

game1 = Game("Football",11,5)
print(game1.__dict__.keys())
print(game1.__dict__.values())  
  # This means object_name.__dict__ returns a dictionary of the object's attributes and their values without using dir().



for attr in dir(game1):
    if not attr.startswith('__')  and not callable(getattr(game1,attr)):
        value = getattr(game1,attr)
        print(f'{attr} : {value}')

# not attr.startswith('__') helps us exclude the other attributes of the Python object.
# not callable(getattr(game1, attr)) helps ensure that methods are also excluded.
# Otherwise, it could print something like playing: <bound method Game.playing of <__main__.Game object at 0x0000019865D28590>>.




# People can have many social media accounts, and we may not know them all. That is why we create a class with pass
# and add attributes to it later.

class Socials:
    pass

justin_socials = Socials()
justin_socials.twitter = "x.com/irmjustin"
print(justin_socials.twitter)  # Direct assignment.


setattr(justin_socials,"github","github.com/irmjustin")
setattr(justin_socials,"tiktok","tiktok.com/@stin250")
print(justin_socials.github)

# if we are google or any other company is going to hire  someone they  may not need his snapchat so to avoid useless data
# they may need to delete socials like that then they may need to first ensure if it is their before they delete 

# We use hasattr() to check whether a certain attribute exists.

print(hasattr(justin_socials,"snapchat")) # False because it hasn't been added.

# or simply  using it with delattr
print(getattr(justin_socials,'tiktok')) # It exists.
if hasattr(justin_socials,'tiktok'):
    delattr(justin_socials,'tiktok')

# print(getattr(justin_socials,'tiktok'))   this will return AttributeError: 'Socials' object has no attribute 'tiktok'
