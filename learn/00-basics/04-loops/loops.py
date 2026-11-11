# Loops.

programming_languages = ['Python','Rust','C++','Javascript','Java','C','PHP']

for language in programming_languages:
    print(language)


# for char in 'Developer': This will print every letter of the word developer on a new line.
#   print(char)    


# Multiplication by 2.
numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    print(f'2  *  {num} = {num * 2}')


# A while loop is useful when you don't know in advance how many repetitions are needed.
age = 0

while age < 18 :
    age = int(input("What is your age ?"))
    if age < 18:
        print("You are not eligible to play betting ")

print("You are eligible")      

# Break and continue.

developer_names = [ 'Justin','John','Paul','Jane','Doe']

for developer in developer_names:
    if developer == 'Paul':
        break
    print(developer)

# If you wanted to print Paul, you would move print(developer) inside the if block.


billionaires = ['Elon Musk','Mark Zuckerberg','Jeff Bezos','Justin Iratuzi','Bill Gates','Alexandr Wang','Cristiano Ronaldo']
# Continue is used to skip to the next iteration of a loop.
for billinaire in billionaires :
    if billinaire == 'Justin Iratuzi':
        continue
    print(billinaire)

# Using else with for and while loops.
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


# Ranges.
# range(start, stop, step)
for num in range(3): # The stop is non-inclusive, so it will print from 0 to 2. Three will not be included.
    print(num)

for num in range(1, 5):
    print(num)    

for num in range(2, 11, 2):
    print(num)    

# If you don't add an argument to range(), it will return a TypeError.

# If you want something in reverse order:

for num in range(60, 0, -10):
    print(num)    

# Creating lists or tuples using the range keyword.

numberz = list(range(10))
print(numberz)

integers = tuple(range(-5,6,1)) # We used 1 as the increment, but this would also work if we didn't specify it because it is there by default.
print(integers)


# Enumerate and zip functions.

games = ['Football','Volleyball','Basket ball','Hand ball','Tennis']

# If you want to print the game and track its index:

index = 0
for game in games:
    print(f'Index : {index} Game : {game}')
    index +=1
# You can use the enumerate function to make this easier.

print(list(enumerate(games)) )   

# or 

for index_1 , game in enumerate(games):
    print(f'index : {index_1} and game : {game}')

# If you want a starting point:
for index_1 , game in enumerate(games,2):
    print(f'index : {index_1} and game : {game}') 

ai_engineers = ['Andrej Karpathy','Ilya Sutskever','Alexandr Wang']
ids = [1,2,3]

print(list(zip(ids,ai_engineers)))

for name, dev_id in zip(ai_engineers, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')
