# dictonaries are built-in data structures that store collections of key-value pairs

# declaring and assigning dictonaries
student = {
    'name':'John Doe',
    'age': 19,
    'school':'Rwanda Coding Academy',
    'field': 'Computer Science',
    'hobbies': ['Football','Sing and Dance','Open Source Contributions']
}

# using dict() constructor
teacher = dict([('name','Paul'),('age',32),('subject','Mathematics')])

#accessing dictonaries 
print(f'{student['name']} is taught {teacher['subject']} by {teacher['name']}')

# updating 
teacher['name']= 'Emmanuel'

#note that if you use the key that didn't exist it will create the new one or you can use the same way adding the new key 
teacher['degree']=  'Phd in Mathematics'

print(f'{teacher['name']} {teacher['degree']} is {teacher['age']} years old')

# some methods to perform common operatioins on dictonariers

print(student.get('hobbies'))
print(student.get('country')) # if the key specified doesn't exist it will return none  or simply you can set the default value to return if the key doesn't exist
print(teacher.get('hobbies',[])) # this will return an empty list because hobbies key doesn't exist in teacher dictonary
print(teacher.get('age',0)) # this will return 32 as age but if the age didn't exist it would have returned 0

# .keys() and .values()

student_keys = student.keys() # returns the list of the keys in student dictonary
student_values =student.values()# returns student values
print(student_keys,student_values)  

# .items() returns both the keys and the values
teacher_items = teacher.items()
print(teacher_items)

# .clear() clears the dictonary
teacher.clear()
print(teacher) # empty dictonary

# .pop()
print(student)
student.pop('age') # removed the age
print(student)
# student.pop('class')  this will return a key error because the class key doesn't exist 
# to prevent the error you can use the return value to be returned if the  key doesn't exist
student.pop('class',0)  

# .popitem() is used to remove the last itme
print(student)
student.popitem()
print(student) # hobbies removed

# update

student.update({'name':"Richard Roe",'country':'Rwanda'}) # country didn't exist it will be new
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

# if you want to add a discount of 20% to all price 

for product , price in products.items():
    products[product] = round(price * 0.8)

print(products)  

# if you want to keep tracking the counter
for product in enumerate(products):
    print(product)
for price in enumerate(products.values()):
    print(price)

for index,product in enumerate(products.items()):
    print(index,product)    

for index,price in enumerate(products.values()):
    print(index,price)    

# if you want to start from a specific number 
for product in enumerate(products,1):
    print(product)   