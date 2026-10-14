"""
=============================================================================
ADVANCED FUNCTIONS IN PYTHON: map, filter, and reduce
=============================================================================
In Python, there are built-in functions that work with other functions as arguments.
These are often called "higher-order functions", and they allow us to perform
common operations on lists and other iterables in an elegant and efficient way.
=============================================================================
"""

import functools
from functools import reduce

# =============================================================================
# 1. MAP FUNCTION
# The map() function applies a given function to every item in an iterable
# (like a list) and returns a new iterator/map object with the results.
# - Length of the resulting list remains the same.
# =============================================================================

numbers = [1, 2, 3, 4, 5]


# Define a function that returns the square of a number
def square(num1):
    return num1**2


# Apply the 'square' function to every element in the 'numbers' list
squared_numbers = list(map(square, numbers))

print(f"--- MAP EXAMPLE ---")
print(f"before mapping -> {numbers}")
print(f"after mapping  -> {squared_numbers}\n")


# =============================================================================
# 2. FILTER FUNCTION
# The filter() function tests every element in an iterable against a boolean
# function (a function that returns True or False).
# - It keeps only the elements for which the function returns True.
# - The size of the resulting list may decrease.
# =============================================================================

# Define a function that checks if a number is even (returns True/False)
def is_even(num):
    return num % 2 == 0


# Filter the 'numbers' list to keep only the even numbers
even_numbers = list(filter(is_even, numbers))

print(f"--- FILTER EXAMPLE ---")
print(f"before filter -> {numbers}")
print(f"after filter  -> {even_numbers}\n")


# =============================================================================
# 3. REDUCE FUNCTION
# The reduce() function (imported from the functools module) takes a function
# and a sequence, and applies the function cumulatively to the items.
# - It collapses an entire list/sequence down to a single cumulative value.
# =============================================================================

# Define a function that adds two numbers together
def add(num1, num2):
    return num1 + num2


# Reduce the 'numbers' list to a single sum value
total_sum = reduce(add, numbers)

print(f"--- REDUCE EXAMPLE ---")
print(f"numbers list   -> {numbers}")
print(f"total_sum      -> {total_sum}")