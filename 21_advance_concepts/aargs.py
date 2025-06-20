def sum(*args): 
    # args is a tuple of all the arguments passed to the function
    total = 0
    for item in args:
        total += item   
    return total
        
print(sum(5, 3,6))

# if we take 
# print(sum(5, 3, 4))  # TypeError: sum() takes 2 positional arguments but 3 were given


#kwargs is used to pass a variable number of keyword arguments to a function.

def marks(**kwargs):
    # kwargs is a dictionary of all the keyword arguments passed to the function
    for item in kwargs:
        print(f"{item}: {kwargs[item]}")
        
marks(english=90, math=95, science=85)        
# Output:
# english: 90   
# math: 95
# science: 85


# combining *args and **kwargs in a function


def func1(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    
func1(1, 2, 3, name="Alice", age=30) 