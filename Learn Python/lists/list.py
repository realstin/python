# lists  

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

## printing even numbers
print(numbers[1::2])


people_and_age = ['John',14,'Jane',16,'Doe']

print(f'Person 1 : {people_and_age[0:2]}') # slicing the  wanted part as a sub list

print(f'Person 2 : {people_and_age[2]} {people_and_age[3]}') # accessing them one by one

print(people_and_age)

del(people_and_age[-1]) # deleting something 

print(people_and_age)

print(len(people_and_age)) # finding the number of items in a list 

people_and_age[0] = 'Paul'
print(people_and_age)


developer = ['Justin',1,['Java','Python','Javascript']]
name,years_of_experience,languages = developer
print(name)
print(years_of_experience)
print(languages)
print(f'Favourite Language -> {developer[2][1]}')

# finding some information in big things

print('Rust' in languages ) # False  it would return true if rust is found in languages for a developer



# some methods used by lists

# adding an item at the end

artists = ['Kendrick Lamar','Drake','YNW Melly','Shakira']
print(artists)
artists.append('Justin Bieber')
print(artists)

local_artists = ['Riderman','Amalon','Racine']

# artists.append(local_artists) if you want to add them as a nested array
# to add them as and individual item
artists.extend(local_artists)
print(artists)

#adding items at a specific index 

artists.insert(1,'Rema')
print(artists)

# removing an item  remove() methods which remove only the first occurance

artists.remove('Racine')
print(artists)

# removing an item at a specific index

artists.pop(1)
print(artists)

# emptying a list

artists.clear()
print(artists)

random_numbers = [23,45,65,56,43,34,2,345,7,89,90]

# sorting 
random_numbers.sort()
print(random_numbers)

random_numbers_2 = [ 23,12,21,32,43]
sorted_random_numbers_2 = sorted(random_numbers_2)
print(random_numbers_2)
print(sorted_random_numbers_2)


# print(sorted_random_numbers_2.reverse()) this will return none because some list methods modifies list but don't return the modified one they return  None

# reversed_sorted_numbers = reversed(sorted_random_numbers_2) this returns the reverse iterotor object that knows to move through the list back word
print(list(reversed(sorted_random_numbers_2))) # to print the list you can convert them into a list it does not work like sorted()

print(sorted_random_numbers_2) # this is to show you that the reverse didn't change the original one

# if you want to reverse them and change the original one

sorted_random_numbers_2.reverse()
print(sorted_random_numbers_2)



# finding the index of an item in the list
developer_languages_ordered_by_interest= ['Python','Rust','Javascript','Java']

print(developer_languages_ordered_by_interest.index('Python')) 
# if you want to know the developer frst langauge they are interested in you can use the index method 
# and other thing to know if the language don't existed it would have returned the value error

#ist Comprehensions

even_numbers = []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)   

# list comprehensions is the easy way to write the above loop in few lines

other_even_numbers = [num for num in range(20,31) if num % 2 == 0]
print(other_even_numbers)


# other example 

positive_integers = [1,2,3,4,5,6,7,8]
results = []
for integer in positive_integers:
    if integer % 2 == 0:
        results.append((integer,'Even'))
    else:
        results.append((integer,'Odd'))
print(results)      
# the comprehension way is results = [(integer,'Even') if integer % 2 == 0 else (integer,'Odd') for integer in positive_integers] print(results)  
 
# creating a list using filter() it can be used to filter some data in large data sets  basing on a certain situation 
# filter function is takes two arguments the  which we can take as a requirement or check and then the collection to look from 

words = ['sky','Justin','programmer','developer','code','python']

def is_long_word (word): # function that return true or false
    return len(word)>5

long_words= list(filter(is_long_word,words))
print(long_words)


# map() function on lists

some_numbers = [1,2,3,4,5,6,7]

def square (number):
    return number * number

square_of_some_numbers = list(map(square,some_numbers))
print(square_of_some_numbers)

# sum() function as it's name is used to get the sum of the items in a list or a tuple

numberz = [12,45,56,87,90]
sum_of_numberz = sum(numberz)
print(sum_of_numberz)

# you can give it initial value
print(sum(numberz,start=10))  # or you can only write like this print(sum(numberz,10)) also without start would work


# any() and all()

ages = [12,34,56,16]
print(any(age > 18 for age in ages)) #True
print(any(age<10 for age in ages) ) #false
print(all(age > 18 for age in ages)) #False
print(all(age>10 for age in ages))  #True