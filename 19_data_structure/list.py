marks = [45,34 ,23,90,78,56,89,67,45,23,12,34,56,78,90]
mixed = [45, 'hello', 34, 23, 90, 'world', 78, 56, 89, 67, 45, 23, 12, 34, 56, 78, 90]
print(marks)
print(mixed)    

print(marks[0])  # Accessing the first element of the list
print(mixed[1])  # Accessing the second element of the mixed list

print(marks[1:5])  # Slicing the list to get elements from index 1 to 4
print(mixed[2:6])  # Slicing the mixed list to get elements from index 2 to 5

# list methods
# Adding elements to the list
marks.append(100)  # Adding an element to the end of the list
mixed.append('new item')  # Adding a new item to the mixed list
print(marks)  # Printing the updated marks list
print(mixed)  # Printing the updated mixed list

marks.insert(2, 75)  # Inserting an element at index 2
mixed.insert(3, 'inserted item')  # Inserting an item at index 3
print(marks)  # Printing the updated marks list after insertion
print(mixed)  # Printing the updated mixed list after insertion


marks.pop() # will remove the last element from the marks list
print(marks)
mixed.pop() # will remove the last element from the mixed list
print(mixed)

marks.remove(34)  # Removing the first occurrence of 34 from the marks list
print(marks)  # Printing the marks list after removing 34


mixed.remove('hello')  # Removing the first occurrence of 'hello' from the mixed list
print(mixed)  # Printing the mixed list after removing 'hello'

#extending the list
marks.extend([88, 99, 100])  # Extending the marks list with new elements   
print(marks)  # Printing the marks list after extending it
mixed.extend(['extra1', 'extra2'])  # Extending the mixed list with new items
print(mixed)  # Printing the mixed list after extending it

# Sorting the list
marks.sort()  # Sorting the marks list in ascending order   
print(marks)  # Printing the sorted marks list
# mixed.sort()  # Sorting the mixed list will raise an error because it contains mixed data types
# mixed.sort()  # Uncommenting this line will raise an error because mixed contains strings and integers
# To sort the mixed list, we need to ensure all elements are of the same type   


#list comprehension

a =5 
table=[]
for i in range(1, 11):
   table.append(a * i)  # Appending the multiplication table of 5 to the list
   print(table)  # Printing the multiplication table of 5
# [5]
# [5, 10]
# [5, 10, 15]
# [5, 10, 15, 20]
# [5, 10, 15, 20, 25]
# [5, 10, 15, 20, 25, 30]
# [5, 10, 15, 20, 25, 30, 35]
# [5, 10, 15, 20, 25, 30, 35, 40]
# [5, 10, 15, 20, 25, 30, 35, 40, 45]
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# Using list comprehension to create the multiplication table of 5
table_comp = [a * i for i in range(1, 11)]  # Creating the multiplication table of 5 using list comprehension
print(table_comp)  # Printing the multiplication table of 5 created using list comprehension