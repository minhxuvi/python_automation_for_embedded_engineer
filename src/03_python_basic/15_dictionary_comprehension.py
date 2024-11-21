"""Dictionary Comprehension."""

D = {"a": 1, "b": 2, "c": 3}
E = {k: v for k, v in D.items() if v % 2 == 0}
print(E)

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longpassword"),
    (3, "username", "1234"),
]

username_mapping = {user[0]: user[1] for user in users}
print(username_mapping)

password_mapping = {user[0]: user[2] for user in users}
print(password_mapping)
