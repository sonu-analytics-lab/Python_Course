# . Tuples and Operations on Tuples

# Create a tuple coordinates = (10, 20) and print both elements.

coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.

# coordinates[0] = 50
# print(coordinates)


# Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple
corlist = list(coordinates)
print(corlist)
# corlist[0] = 50
print(corlist)
coordinates = tuple(corlist)
print(coordinates)
