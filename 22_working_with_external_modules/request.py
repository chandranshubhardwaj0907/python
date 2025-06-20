import requests

r = requests.get("https://api.github.com")
print(r.status_code)  # Output: 200 (OK)
print(r.headers)  # Output: Headers of the response 

with open("response.json", "w") as file:
    file.write(r.text)  # Save the response content to a file
    
    
    