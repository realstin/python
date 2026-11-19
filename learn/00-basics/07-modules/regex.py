import re

sentence = 'Hello World!'

print(re.search('World',sentence)) # <re.Match object; span=(6, 11), match='World'>  the object returned
result = re.search('World',sentence)
print(result.group()) #  World (6, 11)
print(result.span())  #  (6, 11)

print(re.search('essay',sentence)) # None 

# By default, regex matching is case sensitive. This means that the pattern 'Cat' does not match the text cat

name = 'John Doe'
print(re.search('doe',name)) # None bcz we have Doe not doe   
print(re.search('doe',name,re.IGNORECASE))   # <re.Match object; span=(5, 8), match='Doe'>


# Special Sequences and Quantifiers Work in Regular Expressions

# link : https://www.freecodecamp.org/learn/python-v9/lecture-working-with-regular-expressions-python/how-do-special-sequences-and-quantifiers-work-in-regular-expressions
print()
print()
code = 'KN 543D'
print(re.search(r'\d',code)) #<re.Match object; span=(3, 4), match='5'>

print(re.search(r'\d+',code)) # <re.Match object; span=(3, 6), match='543'>

word = 'goooooal'
print(re.search(r'go*al',word)) # <re.Match object; span=(0, 8), match='goooooal'>
print(re.search(r'go*al', 'gal'))
print(re.search(r'go*al', 'goal'))
print(re.search(r'go*al', 'goooal'))

print(re.search(r'colou?r', 'My favorite color is blue')) # <re.Match object; span=(12, 17), match='color'>

print(re.search(r'\d{4}', 'Room 42, built in 1978'))  #<re.Match object; span=(18, 22), match='1978'>

cart = 'You have 3 ITEMS in your cart.'
print(re.search(r'\d+ items', cart, re.IGNORECASE)) # <re.Match object; span=(9, 16), match='3 ITEMS'>
 
print(re.search(r'\d{2,4}', '54252524335')) # <re.Match object; span=(0, 4), match='5425'>

print(re.findall(r'\w', 'Justin_12-3!')) # ['J', 'u', 's', 't', 'i', 'n', '_', '1', '2', '3'] - and ! not included

print(re.findall(r'\s','Justin\t is a python lover'))  # ['\t', ' ', ' ', ' ', ' ']

print(re.findall(r'\D','Justin\t123!@')) # ['J', 'u', 's', 't', 'i', 'n', '\t', '!', '@']  anything that is not a digit


# SOME OTHER FUNCTIONS 

# https://www.freecodecamp.org/learn/python-v9/lecture-working-with-regular-expressions-python/what-are-some-useful-functions-in-the-re-module

#match()
print(re.match(r'\d+', '42 apples')) # <re.Match object; span=(0, 2), match='42'>
print(re.match(r'\d+', 'apples: 42')) # None

#fullmatch()
user_input = '10:30pm'
print(re.search(r'\d+:\d+', user_input)) # <re.Match object; span=(0, 5), match='10:30'>
print(re.fullmatch(r'\d+:\d+', '10:30 pm')) # None
print(re.fullmatch(r'\d+:\d+', '10:30')) # <re.Match object; span=(0, 5), match='10:30'>

#findall()
print(re.findall(r'\d+', 'No numbers here')) # []

#sub()
message = 'Hello , my phone number is 0789 123 456'
print(re.sub(r'\d','*',message)) # Hello , my phone number is **** *** ***
print(re.sub(r'\d','#',message,count=6)) #Hello , my phone number is #### ##3 456
print(re.sub(r'cat','dog','Cat is a cat',flags=re.IGNORECASE)) #dog is a dog