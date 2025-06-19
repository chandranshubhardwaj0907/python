# --------- Basic Decorator Example ---------

# A simple decorator function that wraps another function
def decorator_function(func):
    # This is the wrapper function that adds extra behavior
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper  # Return the wrapper function


# A simple function we want to decorate
def say_hello():
    print("Hello, World!")

# Instead of using @decorator_function, we assign manually
f = decorator_function(say_hello)  # This wraps say_hello inside wrapper
f()  # This will execute the wrapper, which calls say_hello inside it


# --------- Decorator with Arguments Example ---------

# A decorator factory that takes an argument `n` (number of repetitions)
def repeat(n):
    # The actual decorator that wraps the function
    def decorator_repeat(func):
        # The wrapper that runs the function `n` times
        def wrapper(a):
            for i in range(n):
                func(a)  # Call the function with argument `a`
        return wrapper  # Return the wrapper
    return decorator_repeat  # Return the decorator

# Decorate the function to run 3 times every time it's called
@repeat(3)
def say_hello(a):
    print(f"Hello {a}")

# This will print "Hello Chandranshu" three times
say_hello("Chandranshu")

# This will print "Hello Chandra" three times
say_hello("Chandra")
