i=1
while(i<6):
    print("hello world", i)  # prints the string "hello world" followed by the current value of i
    print("hello \" world", i)  # prints the string "hello " world" followed by the current value of i
    print("hey how are you? \n i am good ", i)  # prints the string "hey how are you? \n i am good " followed by the current value of i
    i += 1  # incrementing the value of i by 1 to avoid infinite loop

    # Example: Print even numbers from 2 to 10
    j = 2
    while j <= 10:
        print("Even number:", j)
        j += 2

    # Example: Countdown from 5 to 1
    k = 5
    while k > 0:
        print("Countdown:", k)
        k -= 1