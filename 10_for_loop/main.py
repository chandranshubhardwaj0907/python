for i in range(1,6):
    print("hello world", i)  # prints the string "hello world" followed by the current value of i
    print("hello \" world", i)  # prints the string "hello " world" followed by the current value of i
    print("hey how are you? \n i am good ", i)  # prints the string "hey how are you? \n i am good " followed by the current value of i


# prints the multiplication table of 5 from 1 to 10
for i in range(1,11):
    print(f"5 * {i} = {5*i}")  # prints the multiplication table of 5 from 1 to 10 in a formatted string    

# prints the multiplication table of 5 from 1 to 10 with a separator
for i in range(1,11):
    print(f"5 * {i} = {5*i}", sep=",")  # prints the multiplication table of 5 from 1 to 10 with a comma separator       