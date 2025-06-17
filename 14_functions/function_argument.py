def add(a,b):
    """This function takes two arguments and returns their sum."""
    return a + b

c = add(10, 20)
print("The sum of 10 and 20 is:", c)

def multiply(a, b):
    """This function takes two arguments and returns their product."""
    return a * b    

d = multiply(10, 20)
print("The product of 10 and 20 is:", d)

def subtract(a, b):
    """This function takes two arguments and returns their difference."""
    return a - b    

e = subtract(20, 10)
print("The difference between 20 and 10 is:", e)

#positional arguments
def divide(a, b):
    """This function takes two arguments and returns their quotient."""
    return a / b if b != 0 else "Cannot divide by zero" 
f = divide(20, 10)
print("The quotient of 20 and 10 is:", f)

#default arguments
def power(base, exponent=2):
    """This function takes a base and an optional exponent (default is 2) and returns the base raised to the exponent."""
    return base ** exponent
g = power(5)
print("5 raised to the power of 2 is:", g)

#keyword arguments
def greet(name, greeting="Hello"):
    """This function takes a name and an optional greeting (default is 'Hello') and returns a greeting message."""
    return f"{greeting}, {name}!"       
h = greet(name="Alice")
print(h)  # Output: Hello, Alice!