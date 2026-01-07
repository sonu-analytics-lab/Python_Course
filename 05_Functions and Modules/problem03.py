# 3. Lambda Functions IMP

# Write a lambda function that adds two numbers and test it.

def sum(x, y): return x + y


print(sum(3, 2))


# creat a list [1, 2, 3, 4, 5] and use their squares. map() with a lambda function to get

def square(x): return x*x


list1 = [1, 2, 3, 4, 5]

print(list(map(square, list1)))
