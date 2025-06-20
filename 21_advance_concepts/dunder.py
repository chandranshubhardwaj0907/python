# dunder methof are special methods in Python that start and end with double underscores.

class employee:
    company = "TechCorp"  # Static variable shared by all instances

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self._salary}, Company: {employee.company}"

    def __repr__(self): 
        return f"employee({self.name!r}, {self._salary!r})"
    def __len__(self):
        return len(self.name)
    
    
e = employee("Chandranshu Bhardwaj", 100000)
print(e.name)  # Output: Chandranshu Bhardwaj
print(e._salary)  # Output: 100000  
print(str(e))
print(repr(e))  # Output: employee('Chandranshu Bhardwaj', 100000) # repr is used for debugging and development, providing a detailed string representation of the object.
# The __str__ method is used to define a string representation of the object for end-users.


print(len(e))  # Output: 20 (length of the name)
# The __len__ method is used to define the behavior of the built-in len() function for the object.