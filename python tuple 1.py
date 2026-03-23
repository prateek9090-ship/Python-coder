# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Elements from index 1 to 3:", my_tuple[1:4])

# Looping through a tuple
print("All elements in the tuple:")
for item in my_tuple:
    print(item)

# Tuple length
print("Length of tuple:", len(my_tuple))

# Checking if element exists
if 30 in my_tuple:
    print("30 is present in the tuple")