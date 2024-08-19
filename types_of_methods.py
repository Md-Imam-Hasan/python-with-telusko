class Student:
  school = "MGHS"

  def __init__(self, m1, m2, m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

  def avg(self):
    return (self.m1+self.m2+self.m3)/3
  
  @classmethod
  def school_details(cls):
    return cls.school
  
  @staticmethod
  def info():
    print("this is school information")

st1 = Student(23, 56, 87)
st2 = Student(45, 22, 79)

st2.info()

