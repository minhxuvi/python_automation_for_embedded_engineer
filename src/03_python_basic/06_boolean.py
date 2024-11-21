"""boolean."""

A = 10
B = 10
# comparison
print(A == B)
print(A != B)
print(A > B)
print(A < B)
print(A >= B)
print(A <= B)

# logical
print(A == 10 and B == 10)
print(A == 10 or B == 10)
print(A is not B)

# membership
L = [1, 2, 3]
print(10 in L)
print(10 not in L)

# identity
C = 10
D = 10
print(C is D)
print(C is not D)


# isinstance
print(isinstance(10, int))
print(isinstance(10, str))


# issubclass
class X:
    """X."""


class Y(X):
    """Y."""


print(issubclass(Y, X))  # True because Y is a subclass of X
print(issubclass(X, Y))  # False because X is not a subclass of Y
