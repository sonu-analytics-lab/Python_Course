# 5. Dictionaries and Dictionary Methods

# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"}

student = {"name": "John", "age": 20, "grade": "A"}

# Print the value of "name" .
print(student["name"])

# Change "grade" to "A+" .
student["grade"] = "A+"
print(student)

# Add a new key "city" with value "Delhi" .
student["city"] = "Delhi"
print(student)


# 2. Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
f = {"A": 99999, "B": 99990, "C": 99991}

print(f.keys())
# values() to get all numbers
print(f.values())

# items() to loop over key-value pairs and print them

for key, value in f.items():
    print(key, value)
