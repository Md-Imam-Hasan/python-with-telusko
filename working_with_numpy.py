from numpy import *
# from numpy import linspace

# vals = array([1,2,3,4,5])

# print(vals)
# print(vals.dtype)

# arr = linspace(3, 15, 4) 

# print(arr)

arr1 = array([1, 2, 3, 4])
arr2 = arr1.view()
arr2[0] = 1022

print(arr1)
print(arr2)