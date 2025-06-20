# walrus operator


while(data:=input("Enter a number")):
    print(f"You entered: {data}")
    if data == "exit":
        break
    # The walrus operator (:=) allows assignment and evaluation in a single expression.
    # In this example, it assigns the user input to 'data' and checks its value in the while loop condition.
    # This reduces code duplication and can make code more concise.
      
      