"""
Optimal Solution: Bank Loan Risk Assessment System
Topic: Python Conditionals (if, elif, else) & Logical Operators
Level: Beginner (No functions, no try/except, running as a script)
"""

print("=== Welcome to the Bank Loan Risk Assessment System ===")

# Step 1: Input collection (assuming valid inputs based on user instructions)
age = int(input("Enter customer's age: "))
monthly_salary = float(input("Enter monthly net salary (ILS): "))
requested_amount = float(input("Enter requested loan amount (ILS): "))
credit_score = int(input("Enter credit score (300-850): "))
employment_status = input("Enter employment status (employee / freelance / unemployed): ").strip().lower()

# Step 2: Fail-Fast Validation (Immediate rejections)
# Check age boundaries (must be between 18 and 70 inclusive)
if age < 18 or age > 70:
    print("\nDecision: REJECTED")
    print("Reason: Customer is not within the allowed age range (18-70).")

# Check employment status
elif employment_status == "unemployed":
    print("\nDecision: REJECTED")
    print("Reason: Unemployed status does not meet the minimum requirement.")

# Step 3: Risk Evaluation based on Credit Score and Salary (executed only if past fail-fast checks)
else:
    # Low Credit Score (Below 600) -> Automatic rejection
    if credit_score < 600:
        print("\nDecision: REJECTED")
        print("Reason: Loan rejected due to low credit score (below 600).")

    # Excellent Credit Score (750 and above)
    elif credit_score >= 750:
        annual_salary = monthly_salary * 12
        # Condition: High salary (>10,000) and requested amount is <= 5 times the annual salary
        if monthly_salary > 10000 and requested_amount <= (annual_salary * 5):
            print("\nDecision: APPROVED AUTOMATICALLY!")
            print("Reason: Excellent credit score, high monthly salary, and safe loan amount relative to annual income.")
        else:
            print("\nDecision: MANUAL REVIEW REQUIRED")
            print("Reason: Excellent credit score, but salary or loan amount ratio did not meet automatic approval criteria.")

    # Medium Credit Score (600 to 749)
    elif 600 <= credit_score <= 749:
        # Check specific rules for employee vs. freelance
        if employment_status == "employee" and monthly_salary > 12000:
            print("\nDecision: APPROVED")
            print("Reason: Medium credit score, employed, and salary exceeds the 12,000 ILS threshold.")
        elif employment_status == "freelance" and monthly_salary > 15000:
            print("\nDecision: APPROVED")
            print("Reason: Medium credit score, freelance, and salary exceeds the 15,000 ILS threshold.")
        else:
            print("\nDecision: MANUAL REVIEW REQUIRED")
            print("Reason: Medium credit score, but salary does not meet the higher requirement for your employment type.")

    else:
        # Fallback safety check
        print("\nDecision: MANUAL REVIEW REQUIRED")
        print("Reason: Application requires special agent evaluation.")