"""Advance set operation."""

A = {1, 2, 3}
B = {2, 3, 4}

# union
print(A | B)
print(A.union(B))

# intersection
print(A & B)
print(A.intersection(B))

# difference
print(A - B)
print(A.difference(B))

# symmetric difference

print(A ^ B)
print(A.symmetric_difference(B))
