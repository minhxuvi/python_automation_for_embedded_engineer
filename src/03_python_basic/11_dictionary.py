"""Dictionary."""

# dictionary
D = {"a": 1, "b": 2, "c": 3}
print(D)
print(D["a"])
print(D.keys())
print(D.values())
print(D.items())

# update dictionary
D["d"] = 4
print(D)

# delete dictionary
del D["d"]
print(D)

# clear dictionary
D.clear()
print(D)

# copy dictionary
D = {"a": 1, "b": 2, "c": 3}
E = D.copy()
print(E)

# nested dictionary
F = {"a": {"aa": 1, "ab": 2}, "b": {"ba": 3, "bb": 4}}
print(F)
print(F["a"]["aa"])

# dictionary comprehension
G = {i: i * 2 for i in range(10)}
print(G)

# dictionary unpacking
H = {"a": 1, "b": 2, "c": 3}
a, b, c = H
print(a, b, c)
