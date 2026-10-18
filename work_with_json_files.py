"""
This is a tutorial about working with json files in Python for Back-End development.

Key Functions in the 'json' module:
1. json.load(file_object)  - Reads a JSON file directly and parses it into Python data structures (dicts/lists).
2. json.loads(string)      - Parses a JSON-formatted string into Python data structures.
3. json.dump(data, file)   - Serializes Python data and writes it directly into a file.
4. json.dumps(data)        - Serializes Python data into a JSON-formatted string (ideal for API responses).

Important Parameters & Options:
- indent=4                 - Adds clear indentation and line breaks for human readability.
- ensure_ascii=False       - Preserves non-ASCII characters (such as Hebrew, Arabic, etc.) correctly.
- encoding="utf-8"         - Ensures proper character encoding across different operating systems.
"""

import json
import os

USERS_FILE = "users.json"

def load_users() -> list[dict]:
    # Read all dictionaries from json and return them, if file not exists return []
    if not os.path.exists(USERS_FILE):
        return []

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            users_data = json.load(file)
            return users_data
    except json.JSONDecodeError:
        print("Error: File contains invalid JSON syntax.")
        return []
    except IOError as e:
        print(f"File read error: {e}")
        return []

def save_user(users_data: list[dict]) -> bool:
    # Save users list to json file with error handling
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as file:
            json.dump(users_data, file, indent=4, ensure_ascii=False)
            return True
    except IOError as e:
        print(f"Failed to save data: {e}")
        return False


def print_all_users() -> None:
    """Prints all users currently saved in the JSON file in a readable format."""
    print("\n--- Current JSON File Users ---")
    all_users = load_users()
    if not all_users:
        print("The file is empty or does not exist yet.")
        return

    for user in all_users:
        print(f"User ID: {user['id']} | Username: {user['username']} | Email: {user['email']} | Active: {user['is_active']}")
    print("-------------------------------\n")


def add_user(username: str, email: str) -> dict:
    # Running with id and added new user to json file
    users_data = load_users()
    new_id = max([u["id"] for u in users_data], default=0) + 1

    new_user = {
        "id": new_id,
        "username": username,
        "email": email,
        "is_active": True
    }

    users_data.append(new_user)
    save_user(users_data)
    print(f"New user added successfully with userid {new_id}")
    return new_user


def update_user_status(user_id: int, is_active: bool) -> bool:
    # Found user by id and update his status is_active
    users_data = load_users()
    user_found = False
    for user in users_data:
        if user["id"] == user_id:
            user["is_active"] = is_active
            user_found = True
            break

    if user_found:
        save_user(users_data)
        print(f"User ID {user_id} status updated successfully to {is_active}")
        return True

    print(f"User ID {user_id} not found")
    return False


# --- Program Execution with Before & After logs ---

print("=== START OF PROGRAM ===")

# state file initial
print("[STEP 1] Printing initial state:")
print_all_users()

# Add new user
print("[STEP 2] Adding a new user ('ron_devops')...")
add_user("ron_devops", "ron@example.com")
print_all_users()

# Update status to user_id=2
print("[STEP 3] Updating status for user ID 2...")
update_user_status(2, True)
print_all_users()

print("=== END OF PROGRAM ===")