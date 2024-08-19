class A:
  def __init__(self):
    print("In A init")

  def feature1():
    print("Feature 1 is working")
  
  def feature2(self):
    print("Feature 2 is working")

class B:
  def __init__(self):
    print("In B init")
  def feature3(self):
    print("Feature 3 is working")

  def feature4(self):
    print("Feature 4 is working")

class C(A, B):
  def __init__(self):
    super().__init__() # Call the parent class constructor
                       # it will call init in A cause of Methos resolution order. Always left to right
    print("In C init")


b=B()

