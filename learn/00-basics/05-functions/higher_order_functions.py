# Closures
# When you nest a function, the nested function can access the scope of the function it is within.
# That is what we call a closure function.

def add_name():
    name= input("What is your name : ")
    def add():                         
        return "Hello "+ name
    return add

# print(add_name()) will return <function add_name.<locals>.add at 0x000002EB725135E0> because this function returns another function, add.

greet = add_name()
print(greet()) # This will work because  greet was equal to return value of add_name()

# It is closure because it is accessing the outer scope variable name




# Decorators
# In Python, a function is an object.
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

def greet():
    name = input("What is your name : ")
    return 'Hello '+ name

# For example, you may want the person's name to always start with a capital letter. We are going to decorate the function so that we don't modify the structure of the greet function.
# Recall that the title() function makes every word in a sentence start with a capital letter.
def add_capitalize(function):
    def wrapper():
        result = function()
        final_result  = result.title()
        return final_result
    return wrapper

greet_with_capitalize = add_capitalize(greet)
print(greet_with_capitalize())

# The function above shows how this works, but Python provides a cleaner way to do it. Look at the code below.

@add_capitalize
def print_language():
    language= input('What is your favourite programming language: ')
    return language+' is a good language'

print(print_language())


# You can add many decorators to a function, and they are evaluated from the bottom up.
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
# This will print WELCOME TO PYTHON JUSTIN. If the decorators were reversed, it would return WELCOME TO PYTHON Justin.


# If it were written like this, it would first capitalize WELCOME TO PYTHON and then add Justin in lowercase.
'''
@adding_value_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())
'''
