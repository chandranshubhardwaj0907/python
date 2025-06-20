class employee:
    company = "TechCorp"  # Static variable shared by all instances

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    #instance method to get the employee's name
    def print_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, Company: {employee.company}")
        
    #static method to sum two numbers 
    @staticmethod   
    def sum( a, b):
        return a + b
        
    #class method to print the company name
    @classmethod    
    def print_company(cls):
        print(f"Company: {cls.company}")
    @classmethod    
    def change_company(cls, new_company):
        cls.company = new_company
     
e1  = employee("Chandranshu Bhardwaj", 100000)
e2 = employee("John Doe", 80000)
# Accessing static variable using class name
print(employee.company)  # Output: TechCorp     
e1.print_info()  # Output: Name: Chandranshu Bhardwaj, Salary: 100000, Company: TechCorp
# Output: Name: Chandranshu Bhardwaj, Salary: 100000, Company: TechCorp
e2.print_info()  # Output: Name: John Doe, Salary: 80000, Company: TechCorp

print(e2.sum(10, 20)  )# Output: 30

print(e1.print_company())  # Output: Company: TechCorp

e1.change_company("NewTechCorp")  # Change company name
print(employee.company)  # Output: NewTechCorp