from numpy import *

arr = array([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
])

print(arr)

m1 = matrix(arr)
m2 = m1

print(m2)

m3 = matrix('1 2 3; 4 5 6; 7 8 9')

print(diagonal(m3))