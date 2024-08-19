class Parent:
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        print("Inside Child")

c = Child()
c.show()  # Output: Inside Child