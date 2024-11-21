"""02_string_formatting."""

# f string formatting
A = 10
B = 3.14
C = 1 + 2j
print(f"a = {A}, b = {B}, c = {C}")

# % string formatting
A = 10
B = 3.14
C = 1 + 2j
# %s is a placeholder for string formatting. It converts the value of the variable to a string using the str() method.
print("a = %d, b = %f, c = %s" % (A, B, C))  # pylint: disable=consider-using-f-string

# string template
S = "Hello {}"
print(S.format("World"))

# lazy string formatting
A = 10
B = 3.14
C = 1 + 2j
print("a = {}, b = {}, c = {}".format(A, B, C))  # pylint: disable=consider-using-f-string

# string formatting with named arguments
A = 10
B = 3.14
C = 1 + 2j
print("a = {a}, b = {b}, c = {c}".format(b=B, c=C, a=A))  # pylint: disable=consider-using-f-string

# string formatting with positional arguments
A = 10
B = 3.14
C = 1 + 2j
print("a = {0}, b = {1}, c = {2}, d={0}".format(A, B, C))  # pylint: disable=consider-using-f-string
