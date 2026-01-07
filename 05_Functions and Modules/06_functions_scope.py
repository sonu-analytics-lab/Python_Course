def sum(a, b):
    # a and b are local variable
    c = a+b
    z = 1  # its called call variable called z which is destroyed after this function return

    return c


z = 8  # it is global variables
print(z)
print(sum(5, 7))
