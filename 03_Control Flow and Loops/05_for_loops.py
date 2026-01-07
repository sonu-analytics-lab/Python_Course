for i in range(1, 6):
    print(i)


# **1. Basic for loop**


# Loop through a list
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

# 2. Using range()

# Print numbers from 0 to 4
for i in range(5):
    print(i)

# 3. Loop with a step**

# You can skip numbers using a step in `range(start, stop, step)`.

print("Print even numbers from 2 to 10")

for i in range(2, 11, 2):
    print(i)


# 4. Loop through a string

# You can loop through each character in a string.

word = "Python"

for letter in word:
    print(letter)


# 5. Nested for loops

# A loop inside another loop. Useful for grids, tables, etc.


# Print a 3x3 grid
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# **6. Loop through a list with index**

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ```
# 0 apple
# 1 banana
# 2 cherry
# ```
