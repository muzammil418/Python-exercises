def add(a, b):
    return a + b

result = add(5, 3)

print(result)

def is_even(n):

    if n % 2 == 0:
        return True
    else:
        return False

result = is_even(10)

print(result)

def greet(name, greeting="Hello"):

    print(f"{greeting}, {name}!")

greet("Ali")

greet("Ali", "Good Morning")