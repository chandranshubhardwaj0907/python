# Method 1: Using single quotes
string1 = 'Hello, World!'

# Method 2: Using double quotes
string2 = "Hello, World!"

# Method 3: Using triple quotes (for multi-line strings)
string3 = """Hello,
World!"""
print(string1)
print(string2)
print(string3)

name = "Chandranshu"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[-2])  # Accessing the second last character

# String concatenation
greeting = "Hello"
name = "Chandranshu"
full_greeting = greeting + " " + name
print(full_greeting)

#string slicing
substring = name[0:5]  # Extracting characters from index 0 to 4
print(substring)  # Output: Chand

print(name[2:-1])  # Output: andranshu (from index 2 to the end)

print(name[0:10:1])
print(name[0:10:2])
print(name[0:10:3])  # This will print every third character from index 0 to 9
print(name[0:10:4])  # This will print every fourth character from index 0 to 9