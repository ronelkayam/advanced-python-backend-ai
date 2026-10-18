"""
=============================================================================
ADVANCED FUNCTION PARAMETERS IN PYTHON: Default & Optional Arguments
=============================================================================
What are default/optional arguments?
Sometimes we want a function to have a default value for certain parameters
if the caller doesn't provide them. This makes functions more flexible and
reduces the need for writing multiple overloaded functions.

Key concepts covered in this file:
1. Default (Optional) Arguments
2. Order of parameters (Mandatory vs. Optional)
3. Flexible Arguments (*args and **kwargs)
=============================================================================
"""

# =============================================================================
# 1. DEFAULT (OPTIONAL) ARGUMENTS
# If the user doesn't provide a value for the parameter, the default value is used.
# =============================================================================


def greet(name, greeting="Hello"):
    """Greets a person. If no greeting is specified, defaults to 'Hello'."""
    return f"{greeting}, {name}!"


print("--- 1. DEFAULT ARGUMENTS ---")
# Calling with both arguments
print(greet("Alice", "Good morning"))

# Calling with only the mandatory argument (uses the default 'Hello')
print(greet("Bob"))
print()


# =============================================================================
# 2. MULTIPLE PARAMETERS WITH DEFAULTS
# Note: Mandatory parameters MUST come before optional (default) parameters!
# =============================================================================


def describe_pet(pet_name, animal_type="dog", age="unknown"):
    """Prints a description of a pet, using default values if not provided."""
    return f"I have a {age} year old {animal_type} named {pet_name}."


print("--- 2. MULTIPLE PARAMETERS WITH DEFAULTS ---")
print(describe_pet("Buddy", "dog", 3))  # Providing all arguments
print(describe_pet("Whiskers", "cat"))  # Using default age
print(describe_pet("Max"))  # Using default animal_type and age
print()


# =============================================================================
# 3. FLEXIBLE ARGUMENTS: *args (Arbitrary Positional Arguments)
# Allows a function to accept any number of positional arguments as a tuple.
# =============================================================================


def sum_all(*numbers):
    """Accepts any amount of numbers and returns their total sum."""
    total = 0
    for num in numbers:
        total += num
    return total


print("--- 3. FLEXIBLE ARGUMENTS (*args) ---")
print(f"Sum of (1, 2): {sum_all(1, 2)}")
print(f"Sum of (5, 10, 15, 20): {sum_all(5, 10, 15, 20)}")
print()


# =============================================================================
# 4. FLEXIBLE KEYWORD ARGUMENTS: **kwargs (Arbitrary Keyword Arguments)
# Allows a function to accept any number of keyword arguments as a dictionary.
# =============================================================================


def print_user_profile(**user_data):
    """Prints all key-value pairs passed as keyword arguments."""
    print("User Profile Details:")
    for key, value in user_data.items():
        print(f"  - {key}: {value}")


print("--- 4. FLEXIBLE KEYWORD ARGUMENTS (**kwargs) ---")
print_user_profile(username="alex123", email="alex@example.com", age=25)