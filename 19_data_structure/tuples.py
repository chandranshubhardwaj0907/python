#tuple 
a = (1, 2, 3, 4, 5 )  # A tuple is defined using parentheses
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Another tuple with more elements
print(a)  # Output: (1, 2, 3, 4, 5)
print(b)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a[2])
# a[3] = 32  # This will raise an error because tuples are immutable  


c = (5,) # tuple with a single element we have to add a comma at the end

#tuple unpacking

d = (1, 2, 3, 4, 5)  # A tuple with multiple elements   

A , B , C, D, E = d  # Unpacking the tuple into multiple variables

print(A)  # Output: 1
print(B)  # Output: 2       
print(C)  # Output: 3
print(D)  # Output: 

#methods

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # A tuple with multiple elements
print(t.count(5))  # Output: 1 (counts the occurrences of 5 in the tuple)

print(t.index(5))  # Output: 4 (returns the index of the first occurrence of 5 in the tuple)


# tuples are faster than list
#safe from unidentified modification