# Tuples are like lists. The only difference is that lists are mutable, while tuples are immutable once created.

countries_in_africa = ('Rwanda','Burundi','Tanzania','Kenya','Nigeria',['Morocco','Egypt','Tunisia'])

print(countries_in_africa)
print(len(countries_in_africa))
print('France' in countries_in_africa)
print(f'Arabic African Countries  {countries_in_africa[5]}')
print(f'First five countries  {countries_in_africa[0:5]}') # Indexing is zero-based, so the fifth item is at index 4. The last index in a slice is not included, which is why the sixth item at index 5 is not printed.

# Accessing tuple items is like accessing list items.

print(countries_in_africa[0])
print(countries_in_africa[-1])

# countries_in_africa[0]= 'Togo' it will return a type error that tuple doesn't support item assignment

# You can also create a tuple using the tuple() constructor.

name = 'Justin'
print(tuple(name))

print('Tanzania' in countries_in_africa)

student = ('John Doe','Computer Science',"PhD")
student_name,field,degree = student
print(student_name)
print(field)
print(degree)

name_of_student,*rest = student
print(rest) # Used to get the remaining data after extracting the data we wanted.


# Because tuples are immutable, most methods that modify them will return an error.

# del countries_in_africa[1] type error that tuple doesn't support item deletion 

# You can try other methods like these:
#countries_in_africa[0]= 'Cameroon'
#countries_in_africa.remove('Rwanda')
#countries_in_africa.insert(1, 'Algeria')
#countries_in_africa.pop()
#countries_in_africa.clear()
#countries_in_africa.sort()
#countries_in_africa.reverse()


# Tuples can also contain mutable objects.

programmer = ("Justin",['Python','C++','Java'])
print(programmer)
programmer[1].append('Rust')
print(programmer)



# METHODS FOR TUPLES  

cities = ('Nairobi','Kigali','Kampala','Kinshasa','Bujumbura','Dodoma','Kigali')

# Counting the number of times an item appears.
print(cities.count('Kigali')) # It would return an error if no argument were added.

# Finding the index where an item appears.
print(cities.index('Kigali')) # It returns the first occurrence.

# print(cities.index('Cairo')) will return a ValueError because 'Cairo' is not found in cities.

# If you want to search starting from a certain index:
print(cities.index('Kigali',2))

# You can also pass an index to stop at if you have a range you want to work with.
#print(cities.index('Kigali',2,5)) it will return an error if it is not their 

# Sorting them.
even_numbers = (2,6,4,12,10,8,20)
print(sorted(even_numbers))

# Reversing them.
print(sorted(even_numbers,reverse = True))

shoes = ('New Balance','Naked Wolf','Versace','Rebook','Air Force','Jordan','Nike','Puma')

print(sorted(shoes)) # by default it sorts them alphabetically 

# If you want to use a key such as length:

print(sorted(shoes,key=len)) 