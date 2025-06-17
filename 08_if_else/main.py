age = int(input("Enter your age: "))  # input function takes input from user and converts it to integer
if(age > 18):
    print("You are a minor" )  # if age is less than 18, print "You are a minor"

if(age>18):
    print("you can drive")
elif(age == 18):
    print("you can drive but you need to take a test")
elif(age == 0):
    print("Hey you are just born yet")    
else:
    print("you cannot drive")    

print("end of program")  # prints "end of program"


