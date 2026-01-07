# 6 Variable Scope and Docstrings
'''
 Write a function  increment() that has a local variable  counter  initialized to 0 
and increments it by 1  each time it is called. Observe whether the value
persists across function calls
'''


def increment():
    counter = 0
    counter += 1
    print(counter)


increment()


'''
Write a function multiply(a, b)  that has a proper docstring explaining what
it does. Then use help (multiply) to display the docstring.

'''


def multiply(a, b):
    ''' This is muliplication of a and b
    parameters 
        a int or float : first number
        b int or float : second number

    return    
      a X b

    '''
    return a * b


print(multiply(3, 4))

print(multiply.__doc__)
help(multiply)
