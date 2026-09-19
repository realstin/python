# functions 

# def key word is used to create functions
def square(number):
    return number ** 2

print(square(9))  # this prints 9 * 9   which is equal to 81

# creating a function using lambda (below is the function to find the square root of the number)

square_root = lambda x : int(x**0.5)
print(square_root(4))

#using lambda in higher functions 
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda number:number%2==0,numbers))
print(even_numbers)


# this program works but it is not good it is difficult to read and maintain 
result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(result)  # 14

# the best code for the above 
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(calculate_expression(3))  # 14