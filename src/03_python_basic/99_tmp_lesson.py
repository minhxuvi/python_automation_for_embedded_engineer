"""tmp lesson."""

# reduce function
from functools import reduce
from itertools import product

L = [1, 2, 3, 4, 5]
list_o = reduce(lambda a, b: a + b, L)
print(list_o)


# recursion
def func_5(n):
    """docstring."""
    if n == 1:
        return 1
    return n * func_5(n - 1)


print(func_5(5))


# closure
def func_6():
    """docstring."""
    a = 10

    def func_7():
        """docstring."""
        nonlocal a
        a = 20
        print(a)

    func_7()
    print(a)


func_6()


# generator
def func_8():
    """docstring."""
    yield from range(10)


G = func_8()
print(next(G))
print(next(G))
print(next(G))


# decorator
def func_9(func):
    """docstring."""

    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper


@func_9
def func_10():
    """docstring."""
    print("hello")


func_10()

# product

L = [1, 2, 3]
M = list(product(L, L))
print(M)
