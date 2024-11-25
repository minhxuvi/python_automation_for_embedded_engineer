"""Unpacking arguments."""


# function unpacking
def func_1(a, b):
    """docstring."""
    print(a + b)


func_1(1, 2)
func_1(*[1, 2])
func_1(**{"a": 1, "b": 2})
