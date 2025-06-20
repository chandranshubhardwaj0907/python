class employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def first_name(self):
        return self.name.split(" ")[0]

    def set_first_name(self, new_first_name):
        l = self.name.split(" ")
        if len(l) > 1:
            self.name = f"{new_first_name} {l[1]}"
        else:
            self.name = new_first_name

e = employee("Chandranshu Bhardwaj", 100000)

e.projects = 6
print(e.projects)             # Output: 6
print(e.first_name())         # Output: Chandranshu

e.set_first_name("Chandra")
print(e.first_name())         # Output: Chandra

e.set_first_name("Chandran")  # Correct way to change first name again
print(e.first_name())         # Output: Chandran

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):            # acts as getter
        return self.__age

    @age.setter
    def age(self, value):     # acts as setter
        if value > 0:
            self.__age = value
        else:
            print("Invalid age!")

student = Student("Chandranshu", 20)
print(student.age)           # 20
student.age = -10            # Invalid age!
print(student.age)           # 20
student.age = 21
print(student.age)           # 21
