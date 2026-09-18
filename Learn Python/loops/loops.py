#loops

programming_languages = ['Python','Rust','C++','Javascript','Java','C','PHP']

for language in programming_languages:
    print(language)


#for char in 'Developer':   This will print every letter of the word developer on a  new line
#   print(char)    


# multiplication by 2
numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    print(f'2  *  {num} = {num * 2}')


# while loop  it is used for things you don't know the time it would happen 
age = 0

while age < 18 :
    age = int(input("What is your age ?"))
    if age < 18:
        print("You are not eligible to play betting ")

print("You are eligible")      

# break and continue 

developer_names = [ 'Justin','John','Paul','Jane','Doe']

for developer in developer_names:
    if developer == 'Paul':
        break
    print(developer)

# if you wanted to print Paul you would remove print(developer) from a for loop bod


billionaires = ['Elon Musk','Mark Zuckerberg','Jeff Bezos','Justin Iratuzi','Bill Gates','Alexandr Wang','Cristiano Ronaldo']
# continue is used to escape something
for billinaire in billionaires :
    if billinaire == 'Justin Iratuzi':
        continue
    print(billinaire)

# using else with for and while loops    
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


# ranges 
# range(start, stop, step)
for num in range(3): # the stop is non - inclusive so it will print from 0 to 2 , three will not be included
    print(num)

for num in range(1, 5):
    print(num)    

for num in range(2, 11, 2):
    print(num)    

# if you don't add an argument in range it will return a type error 

# if you want something in rervese order

for num in range(60, 0, -10):
    print(num)    

# creating  list or tuples using  range key word 

numberz = list(range(10))
print(numberz)

integers = tuple(range(-5,6,1)) #  we made 1 as an increment but also it would work if we don't specify it is their by default
print(integers)