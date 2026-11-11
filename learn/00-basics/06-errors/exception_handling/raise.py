# raise statement

def square_root (number):
    if number < 0:
        raise ValueError("number can't be negative")
    else:
        return number ** 0.5

try:
    print(square_root(-9))
except ValueError as error:
    print(f'Error: {error}')

