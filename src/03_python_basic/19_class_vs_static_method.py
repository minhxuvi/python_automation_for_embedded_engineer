"""Class vs static method."""


class Person:
    """This is a class that demonstrates usage of class and static methods."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        attributes = [f"{key}={value}" for key, value in self.__dict__.items()]
        return f"Person({', '.join(attributes)})"

    @classmethod
    def func_1(cls, *args, **kwargs):
        """This is a class method that demonstrates usage of class methods.
        Class methods have access to the class and can modify class state."""
        cls.args = args
        for key, value in kwargs.items():
            setattr(cls, key, value)
        attributes = [f"{key}={value}" for key, value in cls.__dict__.items()]
        print(f"Person({', '.join(attributes)})")

    @staticmethod
    def func_2():
        """This is a static method that demonstrates usage of static methods.
        Static methods are just like regular functions but they are associated
        with a class. They do not have access to the class or instance."""
        print("static method")

    def func_3(self):
        """This is an instance method that demonstrates usage of an instance.
        Instance methods have access to the instance and the class."""

        print("instance method")


Person.func_1()
Person.func_2()
Person(name="John", age=30).func_3()

# Function vs method

# Method is the correct term for a function in a class.
# Methods and functions are pretty similar to each other.
# The only difference is that a method is called with an object and has the
# possibility to modify data of an object.
# Functions can modify and return data but they dont have an impact on objects
