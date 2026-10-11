# Dictionaries are built-in data structures that store collections of key-value pairs.

# Declaring and assigning dictionaries.
student = {
    'name':'John Doe',
    'age': 19,
    'school':'Rwanda Coding Academy',
    'field': 'Computer Science',
    'hobbies': ['Football','Sing and Dance','Open Source Contributions']
}

# using dict() constructor
teacher = dict([('name','Paul'),('age',32),('subject','Mathematics')])

# Accessing dictionaries.
print(f'{student['name']} is taught {teacher['subject']} by {teacher['name']}')

# updating 
teacher['name']= 'Emmanuel'

# Note that if you use a key that doesn't exist, it will create a new entry. You can add a new key in the same way.
teacher['degree']=  'Phd in Mathematics'

print(f'{teacher['name']} {teacher['degree']} is {teacher['age']} years old')

# Some methods for performing common operations on dictionaries.

print(student.get('hobbies'))
print(student.get('country')) # If the specified key doesn't exist, it will return None. You can also set a default value to return if the key doesn't exist.
print(teacher.get('hobbies',[])) # This will return an empty list because the hobbies key doesn't exist in the teacher dictionary.
print(teacher.get('age',0)) # This will return 32 as the age, but if the age didn't exist, it would return 0.

# .keys() and .values()

student_keys = student.keys() # Returns the keys in the student dictionary.
student_values =student.values()# Returns the student values.
print(student_keys,student_values)  

# .items() returns both the keys and the values.
teacher_items = teacher.items()
print(teacher_items)

# .clear() clears the dictionary.
teacher.clear()
print(teacher) # empty dictonary

# .pop()
print(student)
student.pop('age') # removed the age
print(student)
# student.pop('class')  this will return a key error because the class key doesn't exist 
# to prevent the error you can use the return value to be returned if the  key doesn't exist
student.pop('class',0)  

# .popitem() is used to remove the last item.
print(student)
student.popitem()
print(student) # hobbies removed

# update

student.update({'name':"Richard Roe",'country':'Rwanda'}) # The country key didn't exist, so it will be added.
print(student)

# looping over a dictonary

products = {
    'laptop':990,
    'smartphone':600,
    'tablet': 400,
    'headphones':120
}
for product in products:  # for product in products.keys():
    print(product)

for price in products.values():
    print(price)

for product in products.items():
    print(product)    

for product,price in products.items():
    print(product,price)    

# If you want to apply a 20% discount to all prices:

for product , price in products.items():
    products[product] = round(price * 0.8)

print(products)  

# If you want to keep track of the counter:
for product in enumerate(products):
    print(product)
for price in enumerate(products.values()):
    print(price)

for index,product in enumerate(products.items()):
    print(index,product)    

for index,price in enumerate(products.values()):
    print(index,price)    

# If you want to start from a specific number:
for product in enumerate(products,1):
    print(product)   
