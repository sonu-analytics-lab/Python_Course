# 2.1 Function Arguments & Return Values

'''Write a function full_name(first, last) that takes first name and last name
as parameters and returns a single string in the format  "First Last"
'''


def full_name(first, last):
    return f"{first} {last}"


print(full_name("Sonu", "Singh"))


'''
2. 
Write a function calculate_area(length, width=10) 
that returns the area of a rectangle. 
Test it by calling the function with:
1. Both width and length 
 
2. Only lenth (use default width)
'''


def calculate_area(length, width=10):
    a = length * width
    return a


print(f"The area of triangle is {calculate_area(5, 3)}")
print(calculate_area(5))
