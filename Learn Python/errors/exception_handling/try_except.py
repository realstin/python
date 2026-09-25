# Exception handling is the process of catching and managing errors that occur during the execution of a program, so your code doesn't crash unexpectedly.
# It is is a core part of writing robust and fault-tolerant programs. It allows you to anticipate, catch, and respond to errors in a structured way.

# you can handle errors using try , except , else and finally  to deal with errors 



try :
    divinded = int(input("Enter your number : "))
    divisor = int(input("Enter your divisor : "))
    quotient = divinded / divisor
except ZeroDivisionError as e:
    print(f'Error occured : {e}')  # or simply  you can if you don't add  that as e you can simply say print('You can't divide by zero')
except ValueError as e:     
    print(f'Error occured : {e}')
else:
    print(f'The quotient of your input is ',quotient)    
finally:
    print('This codes run for every input without break anyway') 
