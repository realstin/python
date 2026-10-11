# Sets are built-in Python data structures that are unordered and don't store duplicate values.
# They only contain values of immutable data types, like numbers, strings, and tuples.
# They support mathematical operations like union, intersection, difference, and symmetric difference.

numbers_set = {1,2,3,4,5,6,7,8}

# Empty set.

prime_numbers_set = set()

print(numbers_set)
print(type(prime_numbers_set),type(numbers_set))

random_set = {}  # This is not an empty set; it is a dictionary. The way to create an empty set is shown on line 9.
print(type(random_set)) # <class 'dict'>

numbers_set.add(9) # This adds 9 to the set. If the number already exists, the set won't change because sets don't store duplicates.
print(numbers_set)

# To remove an item, you can use .discard() or .remove().

numbers_set.remove(6) # One item will be removed. If the item doesn't exist, remove will return a KeyError, but discard will not.
print(numbers_set)

numbers_set.discard(10) # No error will be returned. If the number is in the set, it will be removed.
print(numbers_set)

numbers_set.clear() # The items in the set will be cleared.
print(numbers_set) # set()

set_of_integers ={-5,-4,-3,-2,-1,0,1,2,3,4,5}
set_of_positive_integers ={1,2,3,4,5}
set_of_negative_integers = {-5,-4,-3,-2,-1}

print(set_of_positive_integers.issubset(set_of_integers)) # True
print(set_of_integers.issuperset(set_of_negative_integers)) # True

print(set_of_negative_integers.issubset(set_of_positive_integers)) # False
print(set_of_positive_integers.issuperset(set_of_negative_integers)) # False

print(set_of_negative_integers.isdisjoint(set_of_positive_integers)) # True. This checks whether the sets have no intersection.

set_of_digits = {0,1,2,3,4,5,6,7,8,9}
prime_numbers = {2,3,5,7,11,13,17,19}
print(prime_numbers.isdisjoint(set_of_digits)) # False because there is at least one number in common between the sets.




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

# Note: Sets are not always sorted. They may appear sorted for smaller numbers, but for larger numbers, they may not.
# You can use the built-in sorted() function to sort them, but it will return a list, not a set.



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
