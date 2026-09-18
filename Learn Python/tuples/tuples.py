# tuples are like list the only difference is that
#  as lists are mutable the tuples are immutable once created they can't be changed

countries_in_africa = ('Rwanda','Burundi','Tanzania','Kenya','Nigeria',['Morocco','Egypt','Tunisia'])

print(countries_in_africa)
print(len(countries_in_africa))
print('France' in countries_in_africa)
print(f'Arabic African Countries  {countries_in_africa[5]}')
print(f'First five countries  {countries_in_africa[0:5]}') #It is zero based index also so the five  items if at index 4  and on slicing you know the last index is not printed that's why 6th item on index 5 was no printed

# accesing them is like how we do for lists

print(countries_in_africa[0])
print(countries_in_africa[-1])

# countries_in_africa[0]= 'Togo' it will return a type error that tuple doesn't support item assignment

# also you can create a tuple using a tuple() constructor

name = 'Justin'
print(tuple(name))

print('Tanzania' in countries_in_africa)

student = ('John Doe','Computer Science',"PhD")
student_name,field,degree = student
print(student_name)
print(field)
print(degree)

name_of_student,*rest = student
print(rest) # used to get the  remaining data after filtering data we wanted


#because tuples are not immutable most of methods will return an error if they modify it

# del countries_in_africa[1] type error that tuple doesn't support item deletion 

# you can try other like  these
#countries_in_africa[0]= 'Cameroon'
#countries_in_africa.remove('Rwanda')
#countries_in_africa.insert(1, 'Algeria')
#countries_in_africa.pop()
#countries_in_africa.clear()
#countries_in_africa.sort()
#countries_in_africa.reverse()


# tuples also can contain mutable objects 

programmer = ("Justin",['Python','C++','Java'])
print(programmer)
programmer[1].append('Rust')
print(programmer)



# METHODS FOR TUPLES  

cities = ('Nairobi','Kigali','Kampala','Kinshasa','Bujumbura','Dodoma','Kigali')

# counting the appearance of an item
print(cities.count('Kigali')) # it would turn an error if no argument added

# finding the index the item appeared
print(cities.index('Kigali')) # it returns the first occurence

# print(cities.index('Cairo')) it will return a value error because 'Cairo' is not found in cities

# if you want to check starting from a certain index
print(cities.index('Kigali',2))

# you can also pass and index to stop in if you have a range you want to only work with 
#print(cities.index('Kigali',2,5)) it will return an error if it is not their 

#sorting  them 
even_numbers = (2,6,4,12,10,8,20)
print(sorted(even_numbers))

#reversing them 
print(sorted(even_numbers,reverse = True))

shoes = ('New Balance','Naked Wolf','Versace','Rebook','Air Force','Jordan','Nike','Puma')

print(sorted(shoes)) # by default it sorts them alphabetically 

#if you want to use your key like length o

print(sorted(shoes,key=len)) 



