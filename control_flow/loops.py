# Hello! Today I will be working with loops in Python
# I will demonstrate how to use for loops and while loops
# I will try my best to work with loops because honestly they are a bit tricky for me
# Let's start with a simple for loop
# I will use a for loop to print numbers from 1 to 10

for x in range(1, 11):
    print(f"Number: {x}")

# Now I will work with a while loop
# I will create a little program that will continue to ask the user for their name
# until they enter a name that is not empty

while True:
    name = input("Please enter your name (q to quit): ")

    if name == "q":
        print("Have a nice day!")
        break
    elif name == "":
        print("You must enter a name!")
    else:
        print(f"Hello {name}! Nice to meet you!")
        break

# Thank you for viewing my coding journey with loops!
