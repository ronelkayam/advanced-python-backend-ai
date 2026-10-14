"""
Title: Python Dictionary Practice Exercises
Description: A collection of practical dictionary exercises covering
filtering, iteration, dynamic updating, and aggregations.
"""

print("==================================================")
print("  EXERCISE 5: Filtering Doctors (Professors Over 60)")
print("==================================================")

# List of doctor dictionaries containing personal and professional details
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

# Filter and print doctors who are 'prof' and over 60 years old
for doctor in doctors:
    if doctor.get("title") == "prof" and doctor.get("age", 0) > 60:
        print("\n********** Professor Details **********")
        for key, value in doctor.items():
            print(f"{key.capitalize()}: {value}")


print("\n\n==================================================")
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

# Task 3: Dynamically assign hospital information to each patient via user input
print("\n--- Assigning Hospitals to Patients ---")
for patient in patients:
    hospital = input(f"Enter hospital for patient {patient.get('name')}: ")
    patient["hospital"] = hospital

# Display updated patient records
print("\n--- Updated Patient Records ---")
for patient in patients:
    print(f"Name: {patient.get('name')}, Age: {patient.get('age')}, "
          f"Diagnosis: {patient.get('diagnosis')}, Hospital: {patient.get('hospital')}")


print("\n\n==================================================")
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

    # Accumulate salary into department total using .get() with a default value of 0
    dept_totals[dept] = dept_totals.get(dept, 0) + salary

# Display aggregated dictionary results
for dept_name, total_spent in dept_totals.items():
    print(f"Department: {dept_name:<10} | Total Spent: ${total_spent:.2f}")