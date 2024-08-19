class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    

s1 = Student("John", 25)

print(s1)  # here we get the object information, automatically calling s1__str__() method
