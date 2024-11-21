"""Destructuring variables."""

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "dummy": "value",
}

name, age, city, _ = person.values()
print(name)

_, _, _, dummy = person.values()
print(dummy)

# list unpacking
cities = ["New York", "London", "Paris", "Tokyo"]
*_, last = cities
print(last)
head, *_, last = cities
print(head)
*_, n_1, n = cities
print(n_1)
print(cities[-2])
