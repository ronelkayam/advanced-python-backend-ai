"""
An f-string (formatted string literal),
introduced in python 3.6 /
is a fast , readable, and modern way to embed variables and
expressions directly inside string
always the type of variable stay as declaration
"""
# the ols way
# print("my age is :" + 36)  # failed
print("my age is :" + str(36))

name = "Alex"
age = 30
price = 45.6783423452352
# basic variable insertion
print(f"Hello my name is {name} and I am {age} years old")

# Inline Math/ expression
print(f"In 5 years , you will be {age + 5}.")

#String methods
print(f"Name in uppercase is {name.upper()}")

#number formating (2 decimal places)
print(f"Total salary is ${price:.2f}")