"""if statement."""

A = 10
B = 20
C = 30

# simple if statement
if A > B:
    print("a is greater than b")
elif A < B:
    print("a is less than b")
else:
    print("a is equal to b")

# ternary operator
print("a is greater than b") if A > B else print("a is less than b")  # pylint: disable=expression-not-assigned

# nested if statement
if A > B:
    if A > C:
        print("a is greater than b and c")
    else:
        print("a is greater than b but less than c")
else:
    print("a is less than b")
