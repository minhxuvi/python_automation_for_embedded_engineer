"""
Function.

Fucntion vs method:
Method is the correct term for a function in a class.
Methods and functions are pretty similar to each other.
The only difference is that a method is called with an object and has the possibility to modify data of an object.
Functions can modify and return data but they dont have an impact on objects.
"""


# function
def func_1(a, b):
    """docstring."""
    print(a + b)


func_1(1, 2)
func_1(b=2, a=1)


# function with default arguments
def func_2(a=1, b=2):
    """docstring."""
    return a + b


print(func_2())


# type hint
def func_3(a: int, b: int) -> int:
    """docstring."""
    return a + b


print(func_3(1, 2))


# function with variable arguments
def func_4(*args, **kwargs):
    """docstring."""
    print(args)
    print(kwargs)
    return args, kwargs


print(func_4(1, 2, 3, a=1, b=2))
