"""
===================================================================
 Topic: Python Error Handling - Try, Except & Exception Safety
 File: 06_error_handling.py
===================================================================

Description:
This file demonstrates how to handle runtime errors gracefully using 
`try...except` blocks in Python:
1. Preventing Crashes: Catching unexpected errors so the program can 
   continue running instead of stopping abruptly.
2. Specific Exception Catching: Handling different types of errors 
   separately ( ZeroDivisionError vs ValueError) to provide
   clear feedback to the user.
3. Accessing Error Details: Catching the exception object (as e) to log
   technical system details.

Key Takeaways:
- Always place risky code (like user input conversion or math operations) 
  inside the try block.
- Catch specific exceptions first, and always keep your application stable.
"""

print("------ Simple Calculator System --------")

try:
    # Taking input from the user and trying to convert it to an integer
    user_input = input("Enter a number to divide 100 by: ")
    num = int(user_input)

    # Division that might fail if num is 0
    result = 100 / num
    print(f"The result is: {result}")

except ZeroDivisionError as e:
    # Catches division by zero (e.g., user inputs 0)
    print("Error: You cannot divide by zero!")
    print(f"System log -> {e}")

except ValueError as e:
    # Catches invalid integer conversion (e.g., user inputs text like "abc")
    print("Error: You must enter a valid integer!")
    print(f"System log -> {e}")

except Exception as e:
    # Catch-all for any other unexpected errors
    print("An unexpected error occurred!")
    print(f"System log -> {e}")

print("The program continues normally and didn't crash! ")