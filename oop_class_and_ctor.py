"""
===================================================================
 Topic: Introduction to OOP - Classes, Objects, and Constructors
===================================================================

Description:
This file demonstrates the basics of Object-Oriented Programming (OOP)
in Python:
1. Class Declaration: Defining a blueprint (`Dog`).
2. Constructor (`__init__` / c'tor): Initializing instance attributes.
3. Methods: Defining behaviors (`bark`) attached to an object.
4. Instantiation: Creating actual instances (objects) from a class.
5. Attribute Access & Mutation: Reading and updating object attributes.

Key Takeaways:
- `self` refers to the specific instance currently being used.
- Attributes can be accessed and modified directly using dot notation (e.g., `dog.name`).
"""

class Dog:
    # Constructor (c'tor) - Defines attributes for every Dog instance
    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed  # Assigning the breed attribute

    # Method - Action that a Dog object can perform
    def bark(self) -> str:
        return f"{self.name} says woof!"


# --- Program Execution / Example Usage ---
if __name__ == "__main__":
    # 1. Instantiating objects (Creating instances of Dog)
    dog1 = Dog(name="Bony", age=2, breed="Poodle")
    lassi = Dog(name="Lassi", age=2, breed="Rottweiler")

    # 2. Calling a method on an object
    print(f"Bark sound of {dog1.name} -> {dog1.bark()}")

    # 3. Accessing attributes directly
    print(f"Original name of lassi -> {lassi.name}")

    # 4. Modifying an attribute value (Mutation)
    lassi.name = "Asi"
    print(f"Updated name of lassi  -> {lassi.name}")