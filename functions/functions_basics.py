# Hello again! I am Aryan and this is my first time working with functions in Python.
# This is a simple Python script to demonstrate functions basics
# I will start by creating a simple function that greets the user and the name is assigned as a parameter.

def greet_user(name):
    print(f"Hello {name}! ")
    print("I hope you're having a nice day!")


greet_user("Aryan")
# This works!
# Now I will create some simple functions that add, subtract, multiply and divide 2 numbers
# I will also use the return statement


def add(num_1, num_2):
    total = num_1 + num_2
    return total


def subtract(num_1, num_2):
    total = num_1 - num_2
    return total


def multiply(num_1, num_2):
    total = num_1 * num_2
    return total


def divide(num_1, num_2):
    total = num_1 / num_2
    return total


print(add(4, 3))
print(subtract(4, 3))
print(multiply(4, 3))
print(f"{divide(4, 3):.2f}")

# Thank you for viewing my code!
