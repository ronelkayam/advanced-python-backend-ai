"""
=============================================================================
LAMBDA FUNCTIONS IN PYTHON (Anonymous Functions)
=============================================================================
What is a lambda function?
A lambda function is a small, anonymous (nameless) function defined using
the 'lambda' keyword. Unlike regular functions defined with 'def', lambda
functions can only contain a single expression and do not need a 'return'
statement (the expression is evaluated and returned automatically).

Syntax:
    lambda arguments: expression
=============================================================================
"""

# =============================================================================
# 1. BASIC LAMBDA FUNCTION VS REGULAR FUNCTION
# =============================================================================

# Regular function:
def square_regular(x):
    return x ** 2


# Equivalent lambda function (single parameter):
square_lambda = lambda x: x ** 2

print("--- 1. BASIC LAMBDA ---")
print(f"Regular function result: {square_regular(5)}")
print(f"Lambda function result:  {square_lambda(5)}\n")


# =============================================================================
# 2. LAMBDA WITH MULTIPLE PARAMETERS (Arguments)
# A lambda function can accept multiple parameters, separated by commas.
# =============================================================================

# A lambda function that receives two parameters (a and b) and adds them
add = lambda a, b: a + b

print("--- 2. MULTIPLE PARAMETERS ---")
print(f"Addition using lambda: 10 + 25 = {add(10, 25)}")

# A lambda function with a conditional (ternary operator) for multiple parameters
max_num = lambda x, y: x if x > y else y
print(f"Max between 10 and 25 is: {max_num(10, 25)}\n")


# =============================================================================
# 3. LAMBDA WITH MAP (Transforming lists)
# =============================================================================

numbers = [1, 2, 3, 4, 5]

# Using lambda directly inside map
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("--- 3. LAMBDA WITH MAP ---")
print(f"Original numbers: {numbers}")
print(f"Doubled (mapped): {doubled_numbers}")

# Advanced: map with multiple lists and a multi-parameter lambda
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sum_two_lists = list(map(lambda x, y: x + y, list1, list2))
print(f"Summing two lists element-by-element: {sum_two_lists}\n")


# =============================================================================
# 4. LAMBDA WITH FILTER (Filtering lists)
# =============================================================================

# Using lambda inside filter to keep only odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("--- 4. LAMBDA WITH FILTER ---")
print(f"Original numbers: {numbers}")
print(f"Odd numbers (filtered): {odd_numbers}\n")


# =============================================================================
# 5. LAMBDA WITH SORTED (Custom sorting)
# =============================================================================

# A list of dictionaries representing students and their grades
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort students by grade using a lambda key
sorted_students = sorted(students, key=lambda student: student["grade"])

print("--- 5. LAMBDA WITH SORTED ---")
print("Students sorted by grade:")
for s in sorted_students:
    print(f"  {s['name']}: {s['grade']}")