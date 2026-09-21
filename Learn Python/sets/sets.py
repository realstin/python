# sets are built in python data structures that are unordered , don't store duplicate values 
#  they only contain values of immutable data types like  numbers , strings ,and tuples
# and they support mathematical operations like union , intersection , difference and symmetric difference

numbers_set = {1,2,3,4,5,6,7,8}

# empty set 

prime_numbers_set = set()

print(numbers_set)
print(type(prime_numbers_set),type(numbers_set))

random_set = {}  # this is not an empty set it is a dictonary the way to create empty sets is the one on line 9
print(type(random_set)) # <class 'dict'>

numbers_set.add(9) # it will add 9 in a set if the number already exists sets don's store duplicate values it will keep one set will not change 
print(numbers_set)

# to remove an item you can use .discard() or .remove() 

numbers_set.remove(6) # one will be removed for remove if the item don't exist it will return a Key error but discard will not
print(numbers_set)

numbers_set.discard(10) # no error will be returned but if the number is one 1 will be removed from a set 
print(numbers_set)

numbers_set.clear() # the items in the set will be cleared
print(numbers_set) # set()

set_of_integers ={-5,-4,-3,-2,-1,0,1,2,3,4,5}
set_of_positive_integers ={1,2,3,4,5}
set_of_negative_integers = {-5,-4,-3,-2,-1}

print(set_of_positive_integers.issubset(set_of_integers)) # True
print(set_of_integers.issuperset(set_of_negative_integers)) # True

print(set_of_negative_integers.issubset(set_of_positive_integers)) # False
print(set_of_positive_integers.issuperset(set_of_negative_integers)) # False

print(set_of_negative_integers.isdisjoint(set_of_positive_integers)) # True it is used to check that the sets have no intersection

set_of_digits = {0,1,2,3,4,5,6,7,8,9}
prime_numbers = {2,3,5,7,11,13,17,19}
print(prime_numbers.isdisjoint(set_of_digits)) # False because there atleast one number in common of the sets




#   |   union operator or .union()
even_numbers = {2,4,6,8,10,12,14}
odd_numbers = {1,3,5,7,9,11,13,15}

positive_integers = odd_numbers | even_numbers
print(positive_integers)   # it will return {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15} 


# & intersection operator  or .intersection()
intersection_of_digits_and_prime_numbers = set_of_digits & prime_numbers
print(intersection_of_digits_and_prime_numbers)


# - The Difference operator or .difference()
difference_prime_digits =  prime_numbers - set_of_digits  # the items in set of prime not in digits
difference_digits_prime = set_of_digits.difference(prime_numbers) # the items in digits which are not in prime
print(difference_prime_digits) 
print(difference_digits_prime)


# ^ symmetric difference  or .symmetric_difference()
symmetric_diff_prime_digits = prime_numbers.symmetric_difference( set_of_digits)
print(symmetric_diff_prime_digits)

# NOTES , sets should not always become sorted they may come as sorted for smaller numbers but for big numbers
# they may come when are not sorted  so you may use the built in method .sorted() to sort if you want but it will return the list not the set



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# A |=B   this same as A = A + B  print(A) will return {1, 2, 3, 4, 5, 6}

# A&=B this is the same as A = A.intersection(B) {3,4} will be returned on print(A)

# A-=B  this is the same as A = A.difference(B) or A = A - B so print(A) will be  {1, 2}

A^=B # this is the same as A = A.symmetric_difference(B)  
print(A) # {1, 2, 5, 6}

print(4 in A) # it will return false because set have been changed the new version of set A is on line 89
print(2 in A) # True

# print(A[0]) this will return  a type error 