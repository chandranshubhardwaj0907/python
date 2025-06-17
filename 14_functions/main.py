def average(num1 , num2  , num3):
    return (num1 + num2 + num3) / 3

print("Welcome to the average calculator")
print("This program will calculate the average of three numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

avg = average(num1, num2, num3)

print(f"The average of {num1}, {num2}, and {num3} is {avg}")