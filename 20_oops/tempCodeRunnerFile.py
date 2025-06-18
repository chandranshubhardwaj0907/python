
# #oops # Object Oriented Programming

# # advntage of OOP
# # 1. Code Reusability   
# # 2. Data Hiding
# # 3. Data Abstraction
# # 4. Polymorphism
# # 5. Inheritance


# # 4 pillars of OOP
# # 1. Encapsulation
# # 2. Abstraction 
# # 3. Inheritance
# # 4. Polymorphism 

# # class is a blueprint for creating objects.

# # object is an instance of a class.


# class Employee:
#     company = "hP"
    
#     def get_salary(self):
#         print(self)
#         return 100000
    
# e1 = Employee()  # Creating an instance of Employee class
# print(e1.company)  # Accessing class variable
# print(e1.get_salary())  # Accessing instance method using class name

# e2 =  Employee()  # Creating another instance of Employee class
# print(e2.company)  # Accessing class variable from another instance 
# print(e2.get_salary())  # Accessing instance method from another instance
# # Note: Both instances share the same class variable 'company' and method 'get_salary'


# #constructor is a special method that is called when an object is created.

# class EmployeeWithConstructor:
    
#     def __init__(self, name, salary, bond):
#         self.name = name
#         self.salary = salary
#         self.bond = bond
    
#     def get_salary(self):
#         # print(self)
#         return 100000
    
#     def get_info(self):
#         return f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond}"
    
# e1 = EmployeeWithConstructor("John", 50000, 2)  # Creating an instance with constructor
# print(e1.get_salary())  # Accessing instance method using the instance
# print(e1.get_info())  # Accessing another instance method to get employee info
# e2 = EmployeeWithConstructor("Doe", 60000, 3)  # Creating another instance with constructor 
# print(e2.get_salary())  # Accessing instance method from another instance
# print(e2.get_info())  # Accessing another instance method to get employee info

# #instance attributes are variables that belong to the instance of the class.
# #class attributes are variables that belong to the class itself.

# # example of instance attributes and class attributes
# class EmployeeWithAttributes:
#     company = "hP"  # class attribute
    
#     def __init__(self, name, salary,company):
#         self.name = name  # instance attribute
#         self.salary = salary  # instance attribute
#         self.company = company  # instance attribute, can override class attribute
    
#     def get_info(self):
#         return f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}"

# e1 = EmployeeWithAttributes("Alice", 70000, "croma")  # Creating an instance
# print(e1.get_info())  # Accessing instance method to get employee info

# #inheritance is a way to form new classes using classes that have already been defined.

# class Animal:
#     location = "India"
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return f"{self.name} makes a sound"
    
# class Dog(Animal):  # Dog class inherits from Animal class
#     def speak(self):
#         return f"{self.name} barks"
    
# a  = Animal("Generic Animal")  # Creating an instance of Animal class
# print(a.speak())  # Accessing speak method of Animal class
# print(a.location)

# d = Dog("Buddy")  # Creating an instance of Dog class
# print(d.speak())  # Accessing overridden speak method of Dog class
# print(d.location)


# #operators overloading is a 