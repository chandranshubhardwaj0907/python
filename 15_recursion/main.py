# 0 1 1 2 3 5  8 13 21 34 55


def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input("Enter a number: "))
if n < 0:
    print("Please enter a non-negative integer.")
elif n > 30:
    print("Please enter a number less than or equal to 30 to avoid long computation times.")
else:
    print(f"Fibonacci of {n} is: ")
print(fib(n))