import time

# Create a large list and tuple
large_list = list(range(10000000))
large_tuple = tuple(range(10000000))

# Time iteration over the list
start_time = time.time()
for item in large_list:
    pass
list_time = time.time() - start_time

# Time iteration over the tuple
start_time = time.time()
for item in large_tuple:
    pass
tuple_time = time.time() - start_time

print(f"Iteration time for list: {list_time:.6f} seconds")
print(f"Iteration time for tuple: {tuple_time:.6f} seconds")
