# Exception handling is the process of catching and managing errors that occur during the execution of a program, so your code doesn't crash unexpectedly.
# It is a core part of writing robust and fault-tolerant programs. It allows you to anticipate, catch, and respond to errors in a structured way.

# You can handle errors using `try`, `except`, `else`, and `finally`.



try :
    divinded = int(input("Enter your number : "))
    divisor = int(input("Enter your divisor : "))
    quotient = divinded / divisor
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')  # If you don't use `as e`, you can simply write print("You can't divide by zero").
except ValueError as e:     
    print(f'Error occurred: {e}')
else:
    print(f'The quotient of your input is ',quotient)    
finally:
    print('This code runs for every input without breaking.')
