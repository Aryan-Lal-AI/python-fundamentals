# Hello again! In this file I am going to to use the type() feature!
# I will also attempt typecasting
# I am going to start with declaring some variables

full_name = "Aryan Lal"
age = 16
gpa = 18.4
is_student = True

# Now I will print the type of each variable

print(type(full_name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Moving forward, I will convert my gpa to an integer

gpa = int(gpa)
print(gpa)

# Now I will convert my age to a float

age = float(age)
print(age)

# I will typecast my age to a string

age = str(age)
print(type(age))

# Finally I’ll check what boolean value my full name holds.

full_name = bool(full_name)
print(full_name)
