# Dictionary: Used to store data in key-value pairs

# Creating a dictionary called 'marks' with student names as keys and their marks as values
marks = {"harry": 34, "jack": 45, "lily": 67}

# Print the dictionary and its type (should show <class 'dict'>)
print(marks, type(marks))

# Access and print the value associated with the key "lily"
print(marks["lily"])

# Update the value of the key "harry" to 3
marks["harry"] = 3
print(marks)

# ---- Dictionary Methods ----

marks.pop("lily")
print(marks)

# Print all the keys in the dictionary
print(marks.keys())

# Print all the values in the dictionary
print(marks.values())

# Clear the entire dictionary (removes all key-value pairs)
print(marks.clear())

# This line will cause an error because the dictionary is now empty after clear()
# marks.pop("lily")
# print(marks)

#dictionary comprehension

table ={i: i*5 for i in range(1,11)}
print(table)
