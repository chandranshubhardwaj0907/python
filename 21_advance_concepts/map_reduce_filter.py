# '''map(): Transforms each element in an iterable using a given function.
# filter(): Filters elements from an iterable based on a condition.
# reduce(): Applies a function cumulatively to the elements of an iterable to reduce it to a single value.
# '''
from functools import reduce
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

new = map(square, numbers)


print(list(new))  # Output: [1, 4, 9, 16, 25]


# filter() is used to filter elements from an iterable based on a condition.
def is_even(x):
    return x % 2 == 0
new = filter(is_even, numbers)
print(list(new))  # Output: [2, 4]  

def is_greater_than_nine(x):
    return x>9

new = filter(is_greater_than_nine, numbers)
print(list(new))  # Output: [] (no elements greater than 9)

new = list(map(lambda x: x * x, numbers)) # using lambda function
print(new)  # Output: [1, 4, 9, 16, 25]  

new = list(filter(lambda x: x % 2 == 0, numbers))  # using lambda function
print(new)  # Output: [2, 4]

#reduce() is used to apply a function cumulatively to the elements of an iterable to reduce it to a single value.

a = [1, 2, 3, 4, 5,6]

def add(x, y):
    return x + y

c = reduce(add,a)
print(c)  # Output: 21 (1 + 2 + 3 + 4 + 5 + 6)


def multiply(x, y ):
    return x * y 
c = reduce(multiply, a)
print(c)  # Output: 720 (1 * 2 * 3 * 4 * 5 * 6)