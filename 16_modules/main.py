# build in module
# import math

# print(math.sqrt(16))  # Output: 4.0
# print(math.factorial(5))  # Output: 120



# external module
import mymodule
import requests
mymodule.hello()  # Output: Hello from mymodule!
r = requests.get('https://www.google.com')
print(r.text)  # Output: HTML content of the Google homepage