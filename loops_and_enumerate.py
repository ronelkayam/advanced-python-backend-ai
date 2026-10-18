"""
This is a tutorial about Python Loops and the 'enumerate()' function.

Why do we need loops?
- Loops allow us to iterate over collections (like lists, tuples, or strings)
  without repeating code manually.

Why do we need 'enumerate()'?
- By default, a standard 'for' loop gives us the item itself, but we lose its position (index).
- 'enumerate()' attaches a counter/index to each item during iteration, saving us from
  managing manual counters or using range(len()).

Key Parameters:
- start=0 (default) - Specifies the starting number forни the index counter.
"""

# --- 1. Regular Loop vs Loop with Enumerate ---
fruits = ["banana", "apple", "cherry"]

print("--- Regular Loop (Item only) ---")
for fruit in fruits:
    print(fruit)

print("\n--- Loop with Enumerate (Index + Item) ---")
# enumerate returns pairs of (index, item)
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# --- 2. Customizing the Starting Index ---
print("\n--- Enumerate with Custom Start (start=1) ---")
tasks = ["Write code", "Run tests", "Deploy to production"]

# start=1 is very useful when presenting numbered lists to humans
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")


# --- 3. Practical Example: Finding an item with its index ---
print("\n--- Practical Example: Searching in a list ---")
users = ["alice", "bob", "charlie", "david"]
target_user = "charlie"

for index, user in enumerate(users):
    if user == target_user:
        print(f"Found '{target_user}' at index {index}!")
        break