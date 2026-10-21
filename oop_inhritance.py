"""
===================================================================
 Topic: Object-Oriented Programming (OOP) - Inheritance
===================================================================

Description:
This file demonstrates the concept of Inheritance in Python:
1. Parent Class (Base Class): A general class containing common attributes
   and methods (Animal).
2. Child Class (Derived Class): A specialized class that inherits from
   the parent class using class Child(Parent) (Cat).
3. super() Function: Used to call the constructor of the parent class
   so we don't repeat code (DRY - Don't Repeat Yourself).
4. Method Extension: The child class inherits parent behavior (eat)
   and adds its own unique behavior (miaow).

Key Takeaways:
- Inheritance promotes code reusability and clear hierarchical relationships.
- Note: Because parent attributes are private (`self.__name`), the child class
  accesses them securely using public getter methods (`self.get_name()`).
"""

# --- Parent Class (Base Class) ---
class Animal:
    def __init__(self, name: str, age: int):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        self.__age = age

    def set_name(self, name: str):
        self.__name = name

    def eat(self) -> str:
        return f"{self.__name} is eating!"


# --- Child Class (Derived Class) ---
class Cat(Animal):
    def __init__(self, name: str, age: int, is_lazy: bool):
        # super() calls the parent class constructor (__init__)
        super().__init__(name, age)
        self.is_lazy = is_lazy  # Unique attribute for Cat

    def miaow(self) -> str:
        # Using parent's getter method because __name is private in Animal
        return f"{self.get_name()} says miaow!"


# --- Program Execution / Example Usage ---

# 1. Instantiating a Cat object (inherits from Animal)
my_cat = Cat("Mizzi", 3, True)

# 2. Calling a method inherited from the Animal parent class
print(my_cat.eat())

# 3. Calling a unique method belonging only to the Cat child class
print(my_cat.miaow())