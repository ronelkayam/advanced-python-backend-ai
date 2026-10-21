"""
===================================================================
 Topic: Object-Oriented Programming (OOP) - Polymorphism
===================================================================

Description:
This file demonstrates the concept of Polymorphism and Duck Typing in Python:
1. Polymorphism: The ability to use a unified interface (the same function
   or method name) to handle different types of objects.
2. Duck Typing: Python's philosophy where the type or class of an object
   doesn't matter; what matters is whether it has the required methods
   or behaviors ("If it walks like a duck and quacks like a duck, it's a duck").
3. Decoupling: The `animal_concert` function doesn't need to know whether
   it's dealing with a Dog, Cat, or Duck—it only cares that the object
   supports the `make_sound()` method.

Key Takeaways:
- We can loop through completely unrelated classes and call the same
  method name, getting unique behavior from each.
"""

class Dog:
    def make_sound(self) -> str:
        return f"woof woof!"

class Cat:
    def make_sound(self) -> str:
        return f"miaow!"

class Duck:
    def make_sound(self) -> str:
        return f"Quack quack"


# Polymorphic function - works with any object that has a 'make_sound' method
def animal_concert(animal_obj) -> None:
    print(animal_obj.make_sound())


# --- Program Execution / Example Usage ---

# 1. Creating a list of different objects (Dog, Cat, Duck)
animals = [Dog(), Cat(), Duck()]

# 2. Iterating through the list and invoking the same function/method dynamically
for animal in animals:
    animal_concert(animal)