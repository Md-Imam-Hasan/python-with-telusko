class A:
  def feature1():
    print("Feature 1 is working")
  
  def feature2(self):
    print("Feature 2 is working")

class B:
  def feature3(self):
    print("Feature 3 is working")

  def feature4(self):
    print("Feature 4 is working")

class C(A, B):
  def feature5(self):
    print("Feature 5 is working")


a = A()
b = B()
c = C()

c.feature2()