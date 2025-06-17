name  = " Chandranshu "
# name[0] ="w" # we cant do this

a = len(name)  # length of string
print(a)  # Output: 12

print(name.lower())  # Convert to lowercase
print(name.upper())  # Convert to uppercase
print(name.title())  # Convert to title case (first letter of each word capitalized)
print(name.strip())  # Remove leading and trailing whitespace

print(name.replace("Chandranshu", "Chandra"))  # Replace a substring
print(name.find("Chandra"))  # Find the index of a substring, returns -1 if not found
print(name.count("a"))  # Count occurrences of a substring
print(name.startswith(" Chand"))  # Check if the string starts with a substring


print(name.isalpha())# Check if the string contains only alphabetic characters
print(name.isdigit())  # Check if the string contains only digits  
print(name.isalnum())  # Check if the string contains only alphanumeric characters
print(name.islower())  # Check if the string is in lowercase


#string formatting
teamplate = "My name is {} and I am {} years old."
name = "Chandranshu"    
age = 21
formatted_string = teamplate.format(name, age)  # Using format method
print(formatted_string)  # Output: My name is Chandranshu and I am 21 years old.

print(f"{a} is the length of the string {name}")  # Using f-string for formatting
# Using f-string for formatting with variables