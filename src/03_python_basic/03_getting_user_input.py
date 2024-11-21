"""03 getting user input."""

name = input("Enter your name: ")
print(f"Hello {name}")

# multiple inputs
first_name, last_name = input("Enter your name: ").split()
print(f"Hello {first_name} {last_name}")
print(last_name)

# input validation
age = input("Enter your age: ")
if age.isdigit():
    print(f"You are {age} years old")
else:
    print("Invalid input")

# input with default value
input_price = input("Enter the price : ")
price: int = int(input_price) if input_price.isdigit() else 0
print(f"You are {price} years old")
