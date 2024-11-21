"""Magic method: __str__ and __repr__.
**Key Differences:**

| Feature | __str__ | __repr__ |
|---|---|---|
| **Purpose** | Human-readable | Unambiguous representation |
| **Use Case** | Logging, display | Debugging, object recreation |
| **Priority** | If not defined, `__repr__` is used | Always defined for clarity |

**Best Practices:**

- **Always define `__repr__`:** It's essential for debugging and introspection.
- **Define `__str__` for user-friendly output:** This provides a more readable representation.
- **Consistency:** Ensure that the output of `__str__` and `__repr__` is consistent and informative.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        Purpose: Provides a human-readable representation of an object.
        Use Case: When you want to print an object in a user-friendly format.
        Example: Used such as for logging or displaying information to the user.
        """
        return f"Person({self.name}, {self.age})"

    def __repr__(self):
        """
        Purpose: Provides a machine-readable representation of an object.
        Use Case: When you want to create a string representation of an object that can be used to recreate the object.
        Example: Used for debugging or serialization.
        """
        return f"Person(name='{self.name}', age={self.age})"


person = Person("John", 30)
print(person)
print(repr(person))
print(str(person))
