# 4. Sets and Set Methods
# 1. Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3 ?)

my_set = {1, 2, 3, 3, 4}
print(my_set)  # remove duplicates


# 2. Add 5 to the set, remove 2 , and check if 4 is in the set.
my_set.add(5)
my_set.remove(2)
print(my_set)

# Create two sets:
a = {1, 2, 3}
b = {3, 4, 5}

# Find their:
# Union
print(a.union(b))

# Intersection
print(a.intersection(b))

# Difference ( a - b )

print(a.difference(b))
