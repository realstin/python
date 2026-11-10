def factorial(number):
    if number ==1 :
        return 1
    result = number * factorial(number-1)
    return result

number = int(input("Which number you want it's factorial : "))
print(factorial(number))