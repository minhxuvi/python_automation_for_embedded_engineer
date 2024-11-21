"""Lambda function."""

# lambda function
lambda_func = lambda a, b: a + b  # pylint: disable=unnecessary-lambda-assignment   # noqa: E731
print(lambda_func(1, 2))

# map function
L = [1, 2, 3, 4, 5]
M = map(lambda a: a * 2, L)
for i in M:
    print(i)


# filter function
L = [1, 2, 3, 4, 5]
N = filter(lambda a: a % 2 == 0, L)
print(list(N))

# alternative way
L = [1, 2, 3, 4, 5]


def func(a):
    """docstring."""
    return a % 2 == 0


N = filter(func, L)
print(list(N))
