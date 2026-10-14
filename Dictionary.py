"""
Title: Python Dictionary Tutorial
Description: A comprehensive guide for students covering Python dictionaries,
key-value pairs, basic operations, methods, and iterations.
"""

# Create a dictionary with student details
student = {
    "name": "Alon",
    "age": 32.5,
    "city": "Modiin",
    "courses": ["Python", "DevOps", "Back-end", "DB", "Math"]
}

# Get all keys as a view/list
print(f"student.keys() -> {student.keys()}")

# Get all values as a view/list
print(f"student.values() -> {student.values()}")

# Print the entire dictionary (with curly braces)
print(f"Full dictionary: {student}")

print("-" * 40)
print("Accessing values by key:")
# Get value by key - throws a KeyError if the key does not exist
print(f"student['name'] -> {student['name']}")
# print(f"student['non_existent'] -> {student['non_existent']}")  # Will raise an error

# Get value safely using .get() method:
# First argument: Desired key
# Second argument: Fallback message if key doesn't exist
print(f"student.get('grade', 'Grade does not exist') -> {student.get('grade', 'Grade does not exist')}")

print("-" * 40)
print("**** Add new variable/key-value pair ****")
print(f"Old dict -> {student}")
student["mail"] = "coder@gmail.com"
print(f"New dict -> {student}")

print("-" * 40)
print("**** Update existing variable ****")
print(f"Old dict -> {student}")
student["mail"] = "walla@gmail.com"  # Updates the value for the existing key 'mail'
print(f"New dict -> {student}")
# Second option to update:
# student.update({"mail": "new_email@gmail.com"})

print("-" * 40)
print("**** Delete a variable/key-value pair ****")
print(f"Old dict -> {student}")
del student["mail"]
print(f"New dict -> {student}")

print("-" * 40)
print("**** Iterations and actions on dictionaries ****")
grades = {
    "Ron": 90,
    "Roni": 100,
    "Joe": 68,
    "John": 70,
    "Mikel": 55,
    "Mike": 40,
    "Sebastian": 95
}

# Iterate through keys only
print("All keys in dictionary:")
for key in grades.keys():
    print(key, end=", ")
print("\n")

# Iterate through values only
print("All values in dictionary:")
for value in grades.values():
    print(value, end=", ")
print("\n")

# Iterate through both keys and values in the same loop using .items()
print("Run all keys & values in the same iteration:")
for key, value in grades.items():
    print(f"Key: {key} -> Value: {value}")