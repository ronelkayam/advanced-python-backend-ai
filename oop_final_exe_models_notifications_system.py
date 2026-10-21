"""
===================================================================
 Topic: Object-Oriented Programming (OOP) - Encapsulation & Data Models
 File: oop_final_exe_models_notifications_system.py
===================================================================

Description:
This file defines the User class, demonstrating the concept of Encapsulation:
1. Public Attributes: user_name can be accessed and modified directly.
2. Private Attributes: __email and __phone_number are hidden from outside
   direct access to protect the object's state.
3. Getters and Setters: Controlled methods (get_email, set_email) that
   allow inspecting and updating private data safely (including validation logic).

Key Takeaways:
- Encapsulation prevents invalid data from entering our system ( ensuring
  an email address contains an '@' sign before saving it).
"""

class User:
    def __init__(self, user_name: str, email: str, phone_number: str):
        self.user_name = user_name          # Public attribute
        self.__email = email                # Private attribute (Encapsulated)
        self.__phone_number = phone_number  # Private attribute (Encapsulated)

    # Getter method - safely exposes the private email
    def get_email(self) -> str:
        return self.__email

    # Setter method - validates and updates the private email securely
    def set_email(self, new_email: str):
        if "@" in new_email:
            self.__email = new_email
            print(f"[Success] Email updated to: {self.__email}")
        else:
            print(f"[Fail] Invalid email address: {new_email}")

    # Getter method - safely exposes the private phone number
    def get_phone_number(self) -> str:
        return self.__phone_number