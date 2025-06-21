try:
    a = int(input("Enter first number: "))

    b = int(input("Enter second number: "))
    
    
    print("what kind of operation do you  want to perform")
    o = input("enter operation (+, -, *, /): ")
    match o:
        case "+":
            print(f"The sum of {a} and {b} is {a + b}")
        case "-":
            print(f"The difference of {a} and {b} is {a - b}")
        case "*":   
            print(f"The product of {a} and {b} is {a * b}")
        case "/":
            if b != 0:
                print(f"The division of {a} by {b} is {a / b}")
            else:
                print("Division by zero is not allowed")
        case _:
            print("Invalid operation. Please enter one of +, -, *, /")
            
except Exception as e:
    print("enter valid numbers")
    
    
    