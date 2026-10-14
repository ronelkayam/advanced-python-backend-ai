"""
=============================================================================
INTRODUCTION TO FUNCTIONS IN PYTHON: Creation, Parameters, and Return Values
=============================================================================
What is a function?
A function is a reusable block of organized code designed to perform a specific
task. Functions help us write cleaner code, avoid repetition (DRY principle),
and break down complex problems into smaller, manageable parts.

Anatomy of a function in Python:
1. 'def' keyword - used to define/create a function.
2. Function name - followed by parentheses '()' and a colon ':'.
3. Parameters (optional) - inputs inside the parentheses that the function accepts.
4. 'return' statement (optional) - sends a result back to where the function was called.
=============================================================================
"""

# =============================================================================
# 1. BASIC FUNCTION (No parameters, no return value)
# A simple function that performs an action (like printing) when called.
# =============================================================================


def func_name():
    print("Hello from func_name function")


print("--- 1. BASIC FUNCTION ---")
print("Hello from main")
# Calling the function twice
func_name()
func_name()
print()


# =============================================================================
# 2. FUNCTION: NO PARAMETERS AND NO RETURN VALUE
# Similar to the first example, this function just executes internal code
# without receiving any inputs or sending back any data.
# =============================================================================


def not_get_and_not_return_func():
    print("Hello from not_get_and_not_return_func")


print("--- 2. NO PARAMETERS, NO RETURN ---")
not_get_and_not_return_func()
print()


# =============================================================================
# 3. FUNCTION: NO PARAMETERS, BUT WITH A RETURN VALUE
# This function does not take any inputs, but it processes data internally
# and returns a result using the 'return' keyword.
# =============================================================================


def not_get_but_returns_func():
    return "This text returned from not_get_but_returns_func"


print("--- 3. NO PARAMETERS, WITH RETURN ---")
text_come_back = not_get_but_returns_func()
print(text_come_back)
print()


# =============================================================================
# 4. FUNCTION: WITH PARAMETERS, BUT NO RETURN VALUE
# This function receives inputs (parameters) when called, performs an action
# using them (like printing), but doesn't return anything.
# =============================================================================


def get_and_not_return_func(x, y):
    print(f"this printing is from get_and_not_return_func: {x} and {y}")


print("--- 4. WITH PARAMETERS, NO RETURN ---")
# Passing values directly
get_and_not_return_func(1, 2)

# Passing variables from the outside
x_out_func = 5
y_out_func = 6
get_and_not_return_func(x_out_func, y_out_func)
print()


# =============================================================================
# 5. FUNCTION: WITH PARAMETERS AND WITH A RETURN VALUE
# The most common type of function. It receives inputs, processes them,
# and returns a final result for further use in the program.
# =============================================================================


def get_and_return_func(name):
    return f"this returned from get_and_return_func: {name} family not found!"


print("--- 5. WITH PARAMETERS AND RETURN ---")
result_message = get_and_return_func("moshe")
print(result_message)