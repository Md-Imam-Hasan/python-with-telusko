from anonymus_functions import *
print(__name__)
def update(x):
  print("before assign x: ",id(x))
  x[1] = 8
  print(id(x))
  print("x",x)


a = [2,3,4];
print(id(a))
update(a)


print("a",a)