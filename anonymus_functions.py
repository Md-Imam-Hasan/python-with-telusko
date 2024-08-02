from functools import reduce

arr = [1, 2, 6, 4, 7, 9, 9, 3, 7, 8, 6]

evens = list(filter(lambda x: x % 2 == 0, arr))
print(evens)

doubles = list(map(lambda x: x * 2, evens))
print(doubles)

sum = reduce(lambda a, b: a + b, doubles)
print(sum)

print(__name__)