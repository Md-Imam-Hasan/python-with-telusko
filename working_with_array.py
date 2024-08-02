from array import *


vals = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    vals.append(x)

for e in vals:
    print(e)

val = int(input("Enter the value to search for: "))

print(vals.index(val))