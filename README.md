# Python and automation course for embedded engineer

## Environment setup

### Install cygwin

https://www.cygwin.com/install.html

Select to install also:

make

### Install python

https://www.python.org/downloads/

Add python path to path environment variable

Set up virtual environment

> python -m venv .venv  
> source .venv/Scripts/activate

### Bash script

Change end of line character of bash script to LF

## Jenkins

## Python basic

### Variables

### String formatting

### Getting user input

### Lists, tuples, and sets

### Advanced set operations

### Booleans in Python

### If statements in Python

### The in keyword

### Loops in Python

### List comprehensions

### Dictionaries

### Destructuring variables

### Functions in Python

### Function arguments and parameters

### Default parameter values

### Functions returning values

### Lambda functions in Python

### Dictionary comprehensions

### Unpacking arguments

### Unpacking keyword arguments

### Object-Oriented Programming in Python

### Magic methods: **str** and **repr**

### Class methods and static methods

### Class inheritance

### Class composition

### Type hinting

### How imports work in Python

### Relative imports in Python

### Errors in Python

### Custom error classes

### First-class functions

### Simple decorators in Python

### The 'at' syntax for decorators

### Decorating functions with parameters

### Decorators with parameters

### Mutability in Python

### Mutable default parameters (and why they're a bad idea)

## Clean code

### Explain SOLID

SOLID is an acronym for five object-oriented design (OOD) principles intended to make software designs more understandable, flexible, and maintainable. These principles were introduced by Robert C. Martin (also known as Uncle Bob) in his book "Agile Software Development: Principles, Patterns, and Practices."

Here's a breakdown of each principle:

1. Single Responsibility Principle (SRP)
   A class should have only one reason to change.
   In other words, a class should have a single responsibility.  
   This principle promotes creating classes with well-defined and focused purposes. By limiting a class's responsibilities, you make it easier to understand, modify, and reuse.

Example:

Instead of having a User class that handles both user data and the process of logging in, you could separate these responsibilities into two classes: User and Authentication.

2. Open/Closed Principle (OCP)
   Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.  
   This principle suggests that you should be able to extend the behavior of a class without modifying its existing code. This is often achieved through inheritance, interfaces, or abstract classes.

Example:

Instead of modifying an existing Shape class to add a new Circle type, you could create a new Circle class that inherits from the Shape class.

3. Liskov Substitution Principle (LSP)
   Subtypes must be substitutable for their base types without altering the correctness of the program.  
   This principle states that objects of a subtype should be able to be used in place of objects of their base type without causing unexpected behavior.

Example:

If you have a Rectangle class and a Square class that inherits from Rectangle, you should be able to use a Square object wherever a Rectangle object is expected without breaking the code.

4. Interface Segregation Principle (ISP)
   Clients should not be forced to depend on interfaces they do not use.  
   This principle suggests that large interfaces should be broken down into smaller, more specific interfaces. This allows clients to only depend on the interfaces they actually need.

Example:

Instead of having a single Printer interface with methods for printing documents, images, and emails, you could create three separate interfaces: DocumentPrinter, ImagePrinter, and EmailPrinter.

5. Dependency Inversion Principle (DIP)
   High-level modules should not depend on low-level modules; both should depend on abstractions.
   Abstractions should not depend on details; details should depend on abstractions.  
   This principle promotes loose coupling between modules by introducing abstractions (interfaces or abstract classes) that mediate the relationship between high-level and low-level modules.

Example:

Instead of a high-level OrderProcessor class directly depending on a low-level Database class, both could depend on an OrderRepository interface. This allows you to easily switch out the database implementation without affecting the OrderProcessor.

Benefits of using SOLID principles:

Increased maintainability: Code becomes easier to understand, modify, and extend.
Improved testability: Classes with well-defined responsibilities are easier to test in isolation.
Better code reusability: Classes that are loosely coupled can be reused in different contexts.
Reduced risk of introducing bugs: Changes to one part of the system are less likely to affect other parts.
By following these principles, you can create more robust, flexible, and maintainable software systems.
