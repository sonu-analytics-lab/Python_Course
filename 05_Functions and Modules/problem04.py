# 4. Recursion in Python
# 1. Write a recursive function factorial(n) that returns the factorial of a

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1)*n


print(factorial(4))

# 2.Write a recursive function sum_of_digits(n) that returns the sum of all digit of a given number


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)


print(sum_of_digits(234))
