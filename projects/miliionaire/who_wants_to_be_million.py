questions = [
             ["What is the capital of France?", "Paris", "London", "Berlin", "Madrid", 1],      
                ["What is 2 + 2?", "3", "4", "5", "6", 2],
                ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 3],
                ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "N2", 1],
                ["Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald", 1]]
prices = [1000, 2000, 3000, 4000, 5000]  # Prices for each question
sum =0
i=0
for question in questions:
    print(question[0])  # Print the question
    print("1.", question[1])  # Print option 1
    print("2.", question[2])  # Print option 2
    print("3.", question[3])  # Print option 3
    print("4.", question[4])  # Print option 4
    
    answer = int(input("Enter your answer (1-4): "))  # Get user input
    if answer == question[5]:  # Check if the answer is correct
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {question[5]}.\n")
        print("Game over!")
        break
    # If the answer is correct, add the price of the question to the total
    sum += prices[i]  # Add the price of the question to the total
    print(f"you won{prices[i]}")    
    i += 1  # Increment the index for the next question 