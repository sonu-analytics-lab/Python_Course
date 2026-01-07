def add(a, b):
    x = a + b
    return x


c = add(11, 5)
print(c)

# --------------------------------
# default argm


def add1(a, b, plus=0):
    x = a + b + plus
    return x


c1 = add1(11, 5, 4)
print(c1)

# --------------------------------
print("keyword arguments")


c1 = add1(b=11, a=5)
print(c1)
