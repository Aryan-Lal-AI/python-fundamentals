# Hello everybody! In this file I am going to use the if-else feature!
# I will also use the input() feature to get user input
# I will start with accepting some user input
# and then I will use if-else statements to check conditions
# Let's assume this is a age checking programme for a credit card

age = int(input("Please enter your age: "))
name = input("Please enter your name:")

if age < 18:
    print(f"Sorry {name}, you're too young to get a credit card!")
elif age > 80:
    print(f"Sorry {name}, you're too old to get a credit card!")
else:
    print(f"Hello {name}! You are {age} years old and eligible to get a credit card!")


# Thank you for viewing!
