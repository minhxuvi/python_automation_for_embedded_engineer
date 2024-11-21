"""the in keyword."""

L = [1, 2, 3]
print(1 in L)
print(4 in L)
print(4 not in L)

if 1 in L:
    print("1 is in L")

if 4 in L:
    print("4 is in L")
else:
    print("4 is not in L")

if 4 not in L:
    print("4 is not in L")
