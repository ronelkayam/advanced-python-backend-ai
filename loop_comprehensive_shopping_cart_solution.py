"""
Optimal Solution: Online Shopping Cart and Daily Sales Analysis System
Topic: Python Loops (while & for), Input Validation, Accumulators, and Counters

Explanation of what this solution does:
1. Interactive Shopping Cart (while loop & validation):
   - Uses a `while` loop to continuously collect product names and prices until the user types 'checkout' or 'סיום'.
   - Implements a nested `while` loop for input validation to ensure that any entered price is strictly greater than 0.
2. Discount Code System (while loop with attempts & break):
   - Gives the user up to 3 attempts to enter a valid promo code from a predefined list.
   - Applies the correct discount percentage and exits the loop immediately using `break` if successful.
3. Daily Sales Analysis (for loop & data accumulation):
   - Iterates over a given list of daily order totals using a `for` loop.
   - Calculates total revenue, finds the highest and lowest purchase amounts, and counts how many orders exceeded 200 ILS.
"""

print("=== Welcome to the Online Shopping Cart & Sales System ===")

# ==========================================
# STEP 1: Interactive Shopping Cart
# ==========================================
subtotal = 0

print("\n--- Step 1: Shopping Cart ---")
print("Enter product name and price. Type 'checkout' or 'סיום' when finished.")

while True:
    product_name = input("Enter product name (or 'checkout' to finish): ").strip()

    # Check for exit condition
    if product_name.lower() in ["checkout", "סיום"]:
        break

    # Input validation for price using a nested while loop
    while True:
        price = float(input(f"Enter price for {product_name}: "))
        if price > 0:
            break
        print("Error: Price must be greater than 0. Please try again.")

    # Accumulate the total subtotal
    subtotal += price

print(f"\nShopping finished! Subtotal before discount: {subtotal:.2f} ILS")

# ==========================================
# STEP 2: Promo Code System (Max 3 attempts)
# ==========================================
print("\n--- Step 2: Promo Code ---")
valid_codes = ["SAVE10", "BLACKFRIDAY", "VIP50"]
attempts = 3
discount_applied = False
final_price = subtotal

while attempts > 0:
    promo_code = input(f"Enter promo code (You have {attempts} attempts left): ").strip()

    if promo_code in valid_codes:
        if promo_code == "SAVE10":
            discount_applied = True
            final_price = subtotal * 0.90  # 10% discount
            print("Success! 10% discount applied.")
        elif promo_code == "BLACKFRIDAY":
            discount_applied = True
            final_price = subtotal * 0.80  # 20% discount
            print("Success! 20% discount applied.")
        elif promo_code == "VIP50":
            discount_applied = True
            final_price = subtotal * 0.50  # 50% discount
            print("Success! 50% discount applied.")

        break  # Exit the loop since a valid code was entered
    else:
        attempts -= 1
        print("Invalid promo code.")

if not discount_applied:
    print("No valid promo code was applied. Continuing with original subtotal.")

print(f"Final price to pay: {final_price:.2f} ILS")

# ==========================================
# STEP 3: Daily Sales Analysis
# ==========================================
print("\n--- Step 3: Daily Sales Analysis ---")

# Sample list of daily order payments
daily_orders = [150.5, 420.0, 89.9, 650.0, 32.0, 210.0]

total_revenue = 0
highest_order = daily_orders[0]  # Initialize with the first item
lowest_order = daily_orders[0]  # Initialize with the first item
orders_over_200 = 0

for amount in daily_orders:
    # 1. Accumulate total revenue
    total_revenue += amount

    # 2. Check for highest order
    if amount > highest_order:
        highest_order = amount

    # 3. Check for lowest order
    if amount < lowest_order:
        lowest_order = amount

    # 4. Count orders above 200 ILS
    if amount > 200:
        orders_over_200 += 1

# Print final daily summary report
print(f"Total Daily Revenue: {total_revenue:.2f} ILS")
print(f"Highest Purchase: {highest_order:.2f} ILS")
print(f"Lowest Purchase: {lowest_order:.2f} ILS")
print(f"Number of orders above 200 ILS: {orders_over_200}")
print("==========================================")