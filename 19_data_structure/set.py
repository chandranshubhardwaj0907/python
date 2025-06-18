# Define a set 's' with some integers (sets are unordered and contain unique elements)
s = {3, 23, 2, 11}

# Print the set and its type (should print <class 'set'>)
print(s, type(s))

# print(s[3])  # This would cause an error because sets do not support indexing

# Add a new element '4' to the set
s.add(4)
print(s)

# Remove the element '2' from the set
s.remove(2)
print(s)

# Discard the element '33' from the set (no error even if the element is not present)
s.discard(33)
print(s)

# Remove a random element from the set (since sets are unordered, you don’t know which one will be removed)
s.pop()

# Check if the element '11' is present in the set and print the result (True/False)
print(11 in s)

# Iterate through each element in the set and print it
for item in s:
    print(item)

# Define two sets 'a' and 'b' with some overlapping and non-overlapping values
a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

# Perform union of sets a and b (all unique elements from both sets)
c = a.union(b)
print(c)

# Perform intersection of sets a and b (common elements only)
d = a.intersection(b)
print(d)

# Find the difference (elements in 'a' that are not in 'b')
e = a.difference(b)
print(e)
