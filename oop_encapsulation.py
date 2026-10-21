"""
===================================================================
 Topic: Object-Oriented Programming (OOP) - Encapsulation
===================================================================

Description:
This file demonstrates the concept of Encapsulation in Python:
1. Public Attributes: Attributes that can be accessed and modified freely 
   from outside the class (e.g., `self.owner`).
2. Private Attributes: Attributes hidden from direct outside access by 
   using a double underscore prefix (e.g., `self.__balance`).
3. Getters & Setters: Controlled methods used to safely inspect or modify 
   private attributes while applying validation rules.

Key Takeaways:
- Encapsulation protects object state from invalid or unauthorized changes.
- Python implements private attributes using "Name Mangling", but using
  public methods (Getters/Setters) is the correct standard practice.
"""

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner          # Public attribute (accessible anywhere)
        self.__balance = balance    # Private attribute (hidden from outside)

    # Getter method - safely exposes the private balance
    def get_balance(self) -> float:
        return self.__balance

    # Controlled modifier method (Action) - updates balance with validation
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to {self.owner}'s account.")
            print(f"New balance: {self.__balance}")
        else:
            print("Error: Invalid deposit amount! Must be greater than 0.")


# --- Program Execution / Example Usage ---

# 1. Instantiating a BankAccount object
acc = BankAccount("Itzik", 1000000.0)

# 2. Accessing a public attribute directly -> Works successfully
print(f"Account owner name: {acc.owner}")

# 3. Trying to access a private attribute directly -> Will fail / AttributeError:
# print(f"owner balance -> {acc.__balance}")

# 4. Accessing the private attribute safely via a Getter method
print(f"Account balance (via getter): {acc.get_balance()}")

# 5. Modifying the state through a controlled method (Deposit)
acc.deposit(100.0)
print(f"Updated balance: {acc.get_balance()}")