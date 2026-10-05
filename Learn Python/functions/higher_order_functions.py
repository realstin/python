# Closures
# When you nest a function that nested function can access the scope of that function it is within 
# and that is what we call Closure Function

def add_name():
    name= input("What is your name : ")
    def add():                         
        return "Hello "+ name
    return add

# print(add_name())will return <function add_name.<locals>.add at 0x000002EB725135E0>   because this function return another function add 

greet = add_name()
print(greet()) # This will work because  greet was equal to return value of add_name()

# It is closure because it is accessing the outer scope variable name




# Decorators
# In Python  , function is an object
#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

def greet():
    name = input("What is your name : ")
    return 'Hello '+ name

# Like you may need to always make the name of person always starting with a capital letter we are going to decorate it so that we don't modify the greet function structure
# Recall title() function it makes every word of sentence start with a capital letter
def add_capitalize(function):
    def wrapper():
        result = function()
        final_result  = result.title()
        return final_result
    return wrapper

greet_with_capitalize = add_capitalize(greet)
print(greet_with_capitalize())

# The above functions shows how things are done but python provides a clean way to do this  look at codes below

@add_capitalize
def print_language():
    language= input('What is you favourite programming language: ')
    return language+' is a good language'

print(print_language())


# You can add many decorators to a function and it evaluates them from down going up 
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def adding_value_decorator(function):
    def wrapper():
        result_with_value = function()
        result_with_value+= " Justin"
        return result_with_value
    return wrapper


@uppercase_decorator
@adding_value_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())  
# this will print WELCOME TO PYTHON JUSTIN if the decorators was inversed it would have return  WELCOME TO PYTHON Justin


# if it was like this below it would first make welcome  to python upper and then lastly add justin not in upper form 
'''
@adding_value_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())
'''
