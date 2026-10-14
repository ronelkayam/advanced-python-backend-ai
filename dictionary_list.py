"""
====================================================================
Title: Python Dictionaries & Lists Guide for Students
Description: A comprehensive tutorial and exercise file covering:
- What a dictionary is and its key advantages.
- Basic operations: creation, access, updates, and deletion.
- Iterating through dictionaries.
- Word frequency counting example.
- Practical exercises (filtering, dynamic inputs, aggregations, and nested data).
====================================================================

WHAT IS A DICTIONARY?
- A dictionary is a collection of variables stored in key-value pairs (key:value).
- Dictionaries are unordered (maintaining insertion order from Python 3.7+), mutable, and fast.
- Enclosed with curly brackets {}.
- Keys must be immutable (strings, numbers, tuples) and UNIQUE.
  If you try to insert a new value with an existing key, it updates the value.
- Values can be of any data type (strings, lists, numbers, or even other dictionaries).
- Very similar to JSON format, making it ideal for working with APIs.
- Elements are separated by commas (,).
"""

# ====================================================================
# PART 1: BASICS & METHODS TUTORIAL
# ====================================================================

# Create a dictionary with student details
student = {
    "name": "Alon",
    "age": 32.5,
    "city": "Modiin",
    "courses": ["Python", "DevOps", "Back-end", "DB", "Math"]
}

# Get all keys as a view
print(f"student.keys() -> {student.keys()}")

# Get all values as a view
print(f"student.values() -> {student.values()}")

# Print the entire dictionary
print(f"Full dictionary: {student}")

print("-" * 50)
print("Accessing values by key:")
# Get value by key - throws a KeyError if the key does not exist
print(f"student['name'] -> {student['name']}")

# Get value safely using .get() method (prevents crashes, allows fallback message)
print(f"student.get('grade', 'Grade does not exist') -> {student.get('grade', 'Grade does not exist')}")

print("-" * 50)
print("**** Add new variable/key-value pair ****")
print(f"Old dict -> {student}")
student["mail"] = "coder@gmail.com"
print(f"New dict -> {student}")

print("-" * 50)
print("**** Update existing variable ****")
print(f"Old dict -> {student}")
student["mail"] = "walla@gmail.com"  # Updates the existing key 'mail'
print(f"New dict -> {student}")

print("-" * 50)
print("**** Delete a variable/key-value pair ****")
print(f"Old dict -> {student}")
del student["mail"]
print(f"New dict -> {student}")

print("-" * 50)
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


print("-" * 50)
print("**** EXAMPLE: Word Frequency Counter ****")
text = "python is great and python is easy"
words = text.split()

word_counts = {}

for word in words:
    # If the word exists, increment its count by 1. Otherwise, start at 0 and add 1.
    word_counts[word] = word_counts.get(word, 0) + 1

print("Word Frequency Results:")
for word, count in word_counts.items():
    print(f"Word: '{word}' -> Count: {count}")


# ====================================================================
# PART 2: PRACTICE EXERCISES
# ====================================================================

print("\n\n" + "=" * 50)
print("  EXERCISE 5: Filtering Doctors (Professors Over 60)")
print("==================================================")

doctors = [
    {
        "name": "mohamad",
        "title": "prof",
        "age": 40,
        "id": 20003332,
        "specialization": "orthopedist",
        "seniority": 15
    },
    {
        "name": "dan",
        "title": "prof",
        "age": 65,
        "id": 20987799,
        "specialization": "cancer",
        "seniority": 35
    },
    {
        "name": "cohen",
        "title": "prof",
        "age": 63,
        "id": 20246675,
        "specialization": "kids",
        "seniority": 25
    },
    {
        "name": "esham",
        "title": "dr",
        "age": 62,
        "id": 20355332,
        "specialization": "generic",
        "seniority": 7
    }
]

for doctor in doctors:
    if doctor.get("title") == "prof" and doctor.get("age", 0) > 60:
        print("\n********** Professor Details **********")
        for key, value in doctor.items():
            print(f"{key.capitalize()}: {value}")


print("\n\n" + "=" * 50)
print("  EXERCISE 8: Patient Records & Dynamic Data Entry")
print("==================================================")

patients = [
    {"name": "Dana", "age": 30, "diagnosis": "flu"},
    {"name": "Yossi", "age": 45, "diagnosis": "diabetes"},
    {"name": "Fatima", "age": 28, "diagnosis": "asthma"}
]

# Task 1: Print all patient names and their ages
print("\n--- All Patients (Name & Age) ---")
for patient in patients:
    print(f"Name: {patient.get('name')}, Age: {patient.get('age')}")

# Task 2: Print details for patients over age 40
print("\n--- Patients Over 40 Years Old ---")
for patient in patients:
    if patient.get("age", 0) > 40:
        print(f"Name: {patient.get('name')}, Age: {patient.get('age')}, Diagnosis: {patient.get('diagnosis')}")

# Task 3: Dynamically assign hospital information via user input
print("\n--- Assigning Hospitals to Patients ---")
for patient in patients:
    hospital = input(f"Enter hospital for patient {patient.get('name')}: ")
    patient["hospital"] = hospital

# Display updated patient records
print("\n--- Updated Patient Records ---")
for patient in patients:
    print(f"Name: {patient.get('name')}, Age: {patient.get('age')}, "
          f"Diagnosis: {patient.get('diagnosis')}, Hospital: {patient.get('hospital')}")


print("\n\n" + "=" * 50)
print("  EXERCISE 9: Employee Payroll Analysis & Aggregation")
print("==================================================")

employees = [
    {"name": "Alice", "department": "DevOps", "hourly_rate": 120, "hours_worked": 45},
    {"name": "Bob", "department": "QA", "hourly_rate": 90, "hours_worked": 38},
    {"name": "Charlie", "department": "DevOps", "hourly_rate": 110, "hours_worked": 50},
    {"name": "David", "department": "QA", "hourly_rate": 95, "hours_worked": 42},
    {"name": "Eve", "department": "Support", "hourly_rate": 70, "hours_worked": 40}
]

# Task 1: Calculate weekly salary including overtime (150% rate for hours > 40)
print("\n--- Task 1: Calculating Weekly Salaries ---")
for emp in employees:
    rate = emp.get("hourly_rate", 0)
    hours = emp.get("hours_worked", 0)

    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_salary = regular_pay + overtime_pay
    else:
        total_salary = hours * rate

    emp["weekly_salary"] = total_salary
    print(f"Employee: {emp['name']}, Hours: {hours}, Weekly Salary: ${total_salary:.2f}")

# Task 2: Filter DevOps employees with weekly salary > 5000
print("\n--- Task 2: High Earning DevOps Employees (> $5000) ---")
for emp in employees:
    if emp.get("department") == "DevOps" and emp.get("weekly_salary", 0) > 5000:
        print(f"Name: {emp['name']}, Salary: ${emp['weekly_salary']:.2f}")

# Task 3: Aggregate total salary spending per department into a new dictionary
print("\n--- Task 3: Total Salary Spending Per Department ---")
dept_totals = {}

for emp in employees:
    dept = emp.get("department")
    salary = emp.get("weekly_salary", 0)
    dept_totals[dept] = dept_totals.get(dept, 0) + salary

for dept_name, total_spent in dept_totals.items():
    print(f"Department: {dept_name:<10} | Total Spent: ${total_spent:.2f}")


print("\n\n" + "=" * 50)
print("  EXERCISE 10: Nested Dictionaries & Grade Averages")
print("==================================================")

students_data = [
    {
        "name": "ron",
        "age": 34,
        "grades": [100, 34, 76, 89, 90]
    },
    {
        "name": "david",
        "age": 30,
        "grades": [100, 34, 55, 90, 90]
    }
]

highest_avg = 0
top_student = ""

print("\n--- Calculating Student Averages ---")
for student in students_data:
    grades_list = student.get("grades", [])
    if len(grades_list) > 0:
        current_avg = sum(grades_list) / len(grades_list)
        print(f"Student: {student.get('name').capitalize()} | Average Grade: {current_avg:.2f}")

        if current_avg > highest_avg:
            highest_avg = current_avg
            top_student = student.get("name")

print(f"\n🏆 Top Student: {top_student.capitalize()} with an average of {highest_avg:.2f}")