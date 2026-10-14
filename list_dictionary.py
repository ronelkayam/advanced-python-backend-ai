"""
====================================================================
Title: Python Lists & Dictionaries Combination Guide
Description: A comprehensive guide focusing on working with lists of
dictionaries (Nested Data Structures), commonly used in APIs and JSON data.
- Creating and accessing lists containing dictionaries.
- Filtering, updating, and modifying nested data structures.
- Practical e-commerce inventory management exercises.
====================================================================

WHAT IS A LIST OF DICTIONARIES?
- In real-world applications (like REST APIs and databases), data is rarely
  just a single dictionary. Instead, it is structured as a LIST of multiple
  objects (dictionaries), where each object represents an entity (e.g., a product,
  a user, or a transaction).
- Structure format:
  items = [
      {"id": 1, "name": "Laptop", "price": 1200},
      {"id": 2, "name": "Mouse", "price": 25}
  ]
- You combine list indexing (e.g., items[0]) with dictionary key access
  (e.g., items[0]["name"]) to navigate through the data.
"""

# ====================================================================
# PART 1: BASICS & TRAVERSING LIST OF DICTIONARIES
# ====================================================================

print("==================================================")
print("  PART 1: Exploring a Product Catalog (E-commerce)")
print("==================================================")

# A list containing multiple product dictionaries
product_catalog = [
    {"product_id": 101, "name": "Wireless Mouse", "category": "Accessories", "price": 45.99, "in_stock": True,
     "tags": ["wireless", "usb", "office"]},
    {"product_id": 102, "name": "Mechanical Keyboard", "category": "Accessories", "price": 120.00, "in_stock": True,
     "tags": ["gaming", "rgb", "mechanical"]},
    {"product_id": 103, "name": "27-inch Monitor", "category": "Displays", "price": 350.50, "in_stock": False,
     "tags": ["4k", "ips", "hdmi"]},
    {"product_id": 104, "name": "USB-C Hub", "category": "Accessories", "price": 30.00, "in_stock": True,
     "tags": ["hub", "adapter", "usb-c"]}
]

# 1. Accessing a specific dictionary in the list by its index
print(f"First product in catalog: {product_catalog[0]['name']} costs ${product_catalog[0]['price']}")

# 2. Iterating through all dictionaries in the list
print("\n--- Listing All Products ---")
for product in product_catalog:
    status = "Available" if product.get("in_stock") else "Out of Stock"
    print(f"[{product.get('category')}] {product.get('name')} - ${product.get('price')} ({status})")

# ====================================================================
# PART 2: MODIFYING AND UPDATING NESTED STRUCTURES
# ====================================================================

print("\n\n==================================================")
print("  PART 2: Modifying Data Inside Lists of Dictionaries")
print("==================================================")

# Let's update the stock status and add a new review score to each product
for product in product_catalog:
    # Simulating a dynamic update: adding a default rating key
    product["rating"] = 4.5

    # If the product is the monitor, let's bring it back in stock
    if product.get("product_id") == 103:
        product["in_stock"] = True

print("Updated Monitor Stock Status (ID 103):")
print(f"Product: {product_catalog[2]['name']} | In Stock: {product_catalog[2]['in_stock']}")

# ====================================================================
# PART 3: PRACTICE EXERCISES
# ====================================================================

print("\n\n==================================================")
print("  EXERCISE 1: Filter and Display Available Accessories")
print("==================================================")

# Task: Print only the products that belong to the 'Accessories' category AND are in stock
print("Available Accessories:")
for product in product_catalog:
    if product.get("category") == "Accessories" and product.get("in_stock") == True:
        print(f" - {product.get('name')} (${product.get('price')})")

print("\n\n==================================================")
print("  EXERCISE 2: Applying a Category-Wide Discount")
print("==================================================")

# Task: Apply a 15% discount to all products in the 'Displays' category,
# update their price, and print the results.
print("Applying 15% discount to 'Displays':")
for product in product_catalog:
    if product.get("category") == "Displays":
        old_price = product.get("price")
        discounted_price = old_price * 0.85  # 15% discount
        product["price"] = round(discounted_price, 2)
        print(f"Product: {product.get('name')} | Old Price: ${old_price} -> New Price: ${product['price']}")

print("\n\n==================================================")
print("  EXERCISE 3: Inventory Valuation & Statistics")
print("==================================================")

# Task: Find and print the most expensive product in the catalog
# and calculate the average price of all products.
highest_price = 0
expensive_product_name = ""
total_price_sum = 0

for product in product_catalog:
    current_price = product.get("price", 0)
    total_price_sum += current_price

    if current_price > highest_price:
        highest_price = current_price
        expensive_product_name = product.get("name")

average_price = total_price_sum / len(product_catalog)

print(f"Catalog Statistics:")
print(f" - Most Expensive Product: {expensive_product_name} (${highest_price})")
print(f" - Average Product Price: ${average_price:.2f}")