def fib(n):
    a,b = 0,1
    while a < n:
        print(a,end=" ")
        a,b = b, a+b
fib(5)  
print()

def fibonacci(number):
    if number == 1:
        return 1
    if number == 0 :
        return 0
    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(3))