"""Class vs static method."""


class Person:
    """This is a class that demonstrates usage of class and static methods."""

    CLS_COUNTER = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        attributes = [f"{key}={value}" for key, value in self.__dict__.items()]
        return f"Person({', '.join(attributes)})"

    @classmethod
    def change_cls_counter(cls):
        """This is a class method that demonstrates usage of class methods.
        Class methods have access to the class and can modify class state."""
        print("class method")
        cls.CLS_COUNTER += 1

    @staticmethod
    def static_method():
        """This is a static method that demonstrates usage of static methods.
        Static methods are just like regular functions but they are associated
        with a class. They do not have access to the class or instance."""
        print("static method")

    def instance_method(self):
        """This is an instance method that demonstrates usage of an instance.
        Instance methods have access to the instance and the class."""

        print("instance method")
        if self.CLS_COUNTER > 0:
            print(f"class attribute is greater than 0 {self.CLS_COUNTER}")
        else:
            self.CLS_COUNTER += 1
            print(f"class attribute is less than 0 {self.CLS_COUNTER}")


if __name__ == "__main__":
    Person.static_method()

    person1 = Person(name="John", age=30)
    person2 = Person(name="John", age=30)
    person1.instance_method()
    print(person1.CLS_COUNTER)
    print(person2.CLS_COUNTER)

    # Person.change_cls_counter()
    person2.instance_method()
    person1.instance_method()


# Function vs method

# Method is the correct term for a function in a class.
# Methods and functions are pretty similar to each other.
# The only difference is that a method is called with an object and has the
# possibility to modify data of an object.
# Functions can modify and return data but they dont have an impact on objects
