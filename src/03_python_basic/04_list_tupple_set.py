"""04 list tupple set."""

# list
L = [1, 2, 3, 3, 2]
print(L)


# tupple
T = (1, 2, 3)
print(T)
print(T[1])


# set
S = {1, 2, 3}
print(S)


# subscript notation available on list, tupple
print(L[0])
L[0] = "Huy"  # type: ignore[call-overload]
print(L[0])
print(T[0])

# append not avalable on tupple and set but available on list
L.append(4)
print(L)

S.add(4)
print(S)

# list to tupple
T_2 = tuple(L)
print(T_2)

# list to set
S_2 = set(L)
print(S_2)

# set to list
L_2 = list(S)
print(L_2)
