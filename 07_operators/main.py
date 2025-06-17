print("Arithmetic operators")
a = 10
b = 20
# addition assignment operator      
# a = a + b  # a = 10 + 20
a += b  # a = a + b, equivalent to a = 10 + 20  
print("a += b:", a)

# subtraction assignment operator
# a = a - b  # a = 30 - 20  
a -= b  # a = a - b, equivalent to a = 30 - 20
print("a -= b:", a)

# multiplication assignment operator
# a = a * b  # a = 10 * 20  
a *= b  # a = a * b, equivalent to a = 10 * 20
print("a *= b:", a)    

# division assignment operator
# a = a / b  # a = 200 / 20
a /= b  # a = a / b, equivalent to a = 200 / 20 
print("a /= b:", a)

# modulus assignment operator   
# a = a % b  # a = 10 % 20  
a %= b  # a = a % b, equivalent to a = 10 % 20
print("a %= b:", a)

# floor division assignment operator
# a = a // b  # a = 10 // 20    
a //= b  # a = a // b, equivalent to a = 10 // 20
print("a //= b:", a)

# exponentiation assignment operator
a =34
b= 2
# a = a ** b  # a = 10 ** 20
a **= b  # a = a ** b, equivalent to a = 10 ** 20
print("a **= b:", a)

print("comparison operators")
# comparison operators --> always return boolean values (True or False)
# These operators are used to compare two values and return a boolean result.
a = 10
b = 20        
print("a == b:", a == b)  # checks if a is equal to b, returns False
print("a != b:", a != b)  # checks if a is not equal to b, returns True
print("a > b:", a > b)    # checks if a is greater than b, returns False
print("a < b:", a < b)    # checks if a is less than b, returns True
print("a >= b:", a >= b)  # checks if a is greater than or equal to b, returns False
print("a <= b:", a <= b)  # checks if a is less than or equal to b, returns True   


print("logical operators")
# logical operators --> always return boolean values (True or False)
# These operators are used to combine multiple boolean expressions and return a boolean result.
a = True    
b = False
print("a and b:", a and b)  # returns False, both conditions must be True
print("a or b:", a or b)    # returns True, at least one condition must be True
print("not a:", not a)      # returns False, negates the value of a

print("Assignment operators")
# assignment operators --> used to assign values to variables
# These operators are used to assign values to variables, often with some operation involved.   
a = 10
b = 20  
# simple assignment operator
# a = b  # assigns the value of b to a      
a = b  # assigns the value of b to a, equivalent to a = 20
# chained assignment operator
# a = b = 30  # assigns the value of 30 to both a and b     
a = b = 30  # assigns the value of 30 to both a and b, equivalent to a = 30 and b = 30
print("a = b = 30:", a, b)  # prints the values of a and b
# augmented assignment operator
# a += 5  # adds 5 to the current value of a    
a += 5  # adds 5 to the current value of a, equivalent to a = a + 5 
print("a += 5:", a)  # prints the value of a after adding 5
# multiple assignment operator
# a, b = 10, 20  # assigns the value of 10 to a and 20 to b
a, b = 10, 20  # assigns the value of 10 to a and 20 to b, equivalent to a = 10 and b = 20  
print("a, b = 10, 20:", a, b)  # prints the values of a and b after multiple assignment

