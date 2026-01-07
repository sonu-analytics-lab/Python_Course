def sum(a, b):
    print("hey I am summing")
    c = a+b
    global z  # this is global z variable
    z = 0  # this will refer to global z  not local variable

    return c


z = 3
print(sum(12, 3))
print(z)
