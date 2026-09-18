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

