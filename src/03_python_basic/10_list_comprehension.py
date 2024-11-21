"""List comprehension."""

L = [1, 2, 3, 4, 5]

print(L)

H = [i * 2 for i in range(10)]
print(H)

LIST_I = [i * 2 for i in range(10) if i % 2 == 0]
print(LIST_I)

J = [i for i in range(10) if i not in L]
print(J)
