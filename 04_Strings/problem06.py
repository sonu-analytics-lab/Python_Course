# 6. Bonus Questions

# Write a program that counts how many vowels are in a given string.

# sentance = "Coding in Python is fun"
# sum = 0
# vowels = ['a', 'e', 'i', 'o', 'u']

# for char in sentance:
#     if char in vowels:
#         sum += 1
# print(f"There are {sum} vowels in this sentance.")


# Take a user input string and check if it is a palindrome (same forwards and backwards).

word = input("Enter your word to check palindrome: ")

if word == word[::-1]:
    print("This is palindrome")
else:
    print("This is not palindrome")
