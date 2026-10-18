"""
=============================================================================
COMPREHENSIVE EXERCISE: Smart Restaurant Order Management System 🍽️
=============================================================================
Estimated Duration: 30-40 minutes.
Objective: Practice advanced Python functions including Type Hints, default
parameters, and flexible arguments (*args and **kwargs).

--- Background ---
You are starting a job at a company that develops POS (Point of Sale) systems
for restaurants. Your task is to write part of the core logic for managing
orders, bills, and customer details.

--- TASKS TO COMPLETE ---

Step 1: Create a Menu Item Function (Type Hints & Default Arguments)
Write a function named `create_menu_item` that accepts:
1. `name` (string) – Item name.
2. `price` (float) – Item price.
3. `category` (string) – Item category, with a default value of "Main Course".
4. `is_vegan` (bool) – Whether the item is vegan, with a default value of False.
The function should return a formatted string, e.g.:
"[Main Course] Pasta - $45.0 (Vegan: False)"

Step 2: Calculate Subtotal Function (*args)
Write a function named `calculate_subtotal` that accepts an arbitrary number
of item prices using `*args` (floats or ints) and returns their total sum (float).

Step 3: Register VIP Customer Function (**kwargs)
Write a function named `register_vip_customer` that accepts a mandatory
`customer_name` string and an arbitrary number of additional details using
`**kwargs`, printing them in a clean, structured format.

Step 4: The Main Integrated Function (`process_order`)
Write a core function that brings everything together:
1. `customer_name` (string) – Mandatory.
2. `tip_percentage` (float) – Optional with a default value of 0.1 (10% tip).
3. `*item_prices` – Arbitrary number of item prices (`*args`).
4. `**extra_info` – Additional info regarding the order (`**kwargs`).
The function should use `calculate_subtotal` to compute the subtotal, add the tip,
print a clean order report, and return the final total to charge (float).
=============================================================================
"""


# =============================================================================
# FULL EXERCISE SOLUTION
# =============================================================================


# Step 1: Create a menu item
def create_menu_item(
    name: str, price: float, category: str = "Main Course", is_vegan: bool = False
) -> str:
  """Returns a formatted string containing menu item details."""
  return f"[{category}] {name} - ${price} (Vegan: {is_vegan})"


# Step 2: Calculate items subtotal
def calculate_subtotal(*prices: float | int) -> float:
  """Accepts an arbitrary number of prices and returns their total sum."""
  total = 0.0
  for price in prices:
    total += float(price)
  return total


# Step 3: Register a VIP customer
def register_vip_customer(customer_name: str, **customer_details: str | int) -> None:
  """Prints customer details along with all dynamic keyword arguments passed."""
  print(f"VIP Customer: {customer_name}")
  for key, value in customer_details.items():
    print(f"  - {key}: {value}")


# Step 4: Main order management function
def process_order(
    customer_name: str, tip_percentage: float = 0.1, *item_prices: float, **extra_info
) -> float:
  """Manages the order: calculates subtotal, tip, prints report, and returns final total."""
  # Call the function from Step 2 to calculate the subtotal of the items
  subtotal: float = calculate_subtotal(*item_prices)

  # Calculate tip and final total price
  tip_amount: float = subtotal * tip_percentage
  final_total: float = subtotal + tip_amount

  print("=" * 40)
  print(f"ORDER SUMMARY FOR: {customer_name}")
  print(f"Subtotal: ${subtotal:.2f}")
  print(f"Tip ({int(tip_percentage * 100)}%): ${tip_amount:.2f}")
  print(f"Final Total to Charge: ${final_total:.2f}")

  # Display extra info if provided (**kwargs)
  if extra_info:
    print("Additional Info:")
    for key, value in extra_info.items():
      print(f"  * {key}: {value}")
  print("=" * 40)

  return final_total


# =============================================================================
# TEST SUITE (Main Execution)
# =============================================================================
if __name__ == "__main__":
  print("--- Testing Step 1: Menu ---")
  print(create_menu_item("Burger", 60.0))
  print(create_menu_item("Tofu Salad", 45.0, "Appetizer", True))
  print()

  print("--- Testing Step 2: Subtotal ---")
  sub = calculate_subtotal(50.0, 30.0, 15.5)
  print(f"Subtotal result: ${sub}")  # Should display 95.5
  print()

  print("--- Testing Step 3: VIP Customer ---")
  register_vip_customer(
      "Alice Smith", phone="050-1234567", email="alice@mail.com", vip_level=2
  )
  print()

  print("--- Testing Step 4: Process Order ---")
  final_bill: float = process_order(
      "Bob Jones",
      0.15,  # 15% tip
      100.0,
      45.5,
      25.0,  # prices (*args)
      delivery_city="Tel Aviv",
      notes="Extra napkins please",  # extra info (**kwargs)
  )
  print(f"Returned Final Bill variable: ${final_bill}")