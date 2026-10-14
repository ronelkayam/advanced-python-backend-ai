"""
=============================================================================
PYTHON CALCULATOR EXAMPLE: Using Functions for Mathematical Operations
=============================================================================
This script demonstrates how to build a basic calculator using user-defined
functions in Python. It covers:
1. The 4 basic arithmetic operations: addition, subtraction, multiplication, division.
2. Advanced math operations: power (exponentiation) and square root (using the math module).
3. Error handling: preventing division by zero.
=============================================================================
"""

import math

# =============================================================================
# 1. BASIC ARITHMETIC FUNCTIONS
# =============================================================================


def plus(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2


def minus(num1, num2):
    """Returns the difference between two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Returns the division of num1 by num2.
    Includes error handling to prevent division by zero."""
    if num2 == 0:
        return "Error: Division by zero is not allowed!"
    return num1 / num2


# =============================================================================
# 2. ADVANCED MATHEMATICAL FUNCTIONS
# =============================================================================


def power(num1, num2):
    """Calculates num1 raised to the power of num2 using a loop."""
    total = 1
    for _ in range(num2):
        total *= num1
    return total


def square(num1):
    """Returns the square root of a number using Python's built-in math module."""
    return math.sqrt(num1)


# =============================================================================
# 3. CALCULATOR EXECUTION & RESULTS
# =============================================================================

print("==============================")
print("     PYTHON CALCULATOR        ")
print("==============================")

num1 = 11234
num2 = 32

print(f"Addition:       {num1} + {num2} = {plus(num1, num2)}")
print(f"Subtraction:    {num1} - {num2} = {minus(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
print(f"Division:       {num1} / {num2} = {divide(num1, num2)}")
print(f"Square Root:    sqrt({num1})  = {square(num1)}")
print(f"Power:          {num1} ^ {num2} = {power(num1, num2)}")
print("==============================")