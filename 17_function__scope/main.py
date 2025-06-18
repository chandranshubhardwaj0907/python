def sum(a,b):
    c= a + b # and b are local variables to this function
    return c

print(sum(1,2))
# This code defines a function `sum` that takes two arguments `a` and `b`, adds them together, and returns the result.


# print(c) # This will raise an error because `c` is not defined in this scope.
# # The variable `c` is defined inside the function `sum`, so it is not accessible outside of that function.

z= 8
print(z) # This will print the value of `z`, which is defined in the global scope.
# The variable `z` is defined outside of any function, so it is accessible anywhere in the module.
# The variable `z` is defined in the global scope, so it can be accessed anywhere in the module.
# If you want to access `c` outside of the function, you would need to return it or define it in the global scope.

#local scope - variables defined inside a function
#global scope - variables defined outside of a function

#using global keyword
def sum(a,b):
    print("Inside function")
    c = a+b
    global z
          # This allows us to modify the global variable z
    z = 10  # This modifies the global variable z
    return c

z=3
print(sum(1,2))  # This will print the result of the sum function
print(z)  # This will print the modified value of z, which is now 10