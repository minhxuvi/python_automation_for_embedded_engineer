"""Object Oriented Programming."""


class Student:
    """docstring."""

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        """docstring."""
        return sum(self.grades) / len(self.grades)


student_1 = Student("John", [70, 80, 90])
print(student_1.name)
print(student_1.average())

student_2 = Student("Jane", [60, 70, 80])
print(student_2.grades)
print(student_2.average())
