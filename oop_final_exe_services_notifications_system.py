"""
===================================================================
 Topic: Object-Oriented Programming (OOP) - Inheritance & Polymorphism
 File: oop_final_exe_services_notifications_system.py
===================================================================

Description:
This file demonstrates Inheritance and Polymorphism in a service architecture:
1. Base Class (BaseNotifier): Contains shared attributes (`provider_name`)
   and common methods (log_delivery) to prevent code duplication (DRY).
2. Derived Classes (SMSNotifier, EmailNotifier): Inherit from BaseNotifier
   using super() and extend functionality with their own specific attributes
   and custom send implementations.
3. Polymorphic Interface: Both derived classes share the same `send` method
   signature, allowing them to be used interchangeably.

Key Takeaways:
- Inheritance creates a logical hierarchy for related services.
- `super()` ensures the parent constructor runs correctly without repeating code.
"""

# --- Base Class (Parent) ---
class BaseNotifier:
    def __init__(self, provider_name: str):
        self.provider_name = provider_name  # Shared attribute for all notifiers

    def log_delivery(self) -> str:
        return f"Logging delivery via {self.provider_name}"


# --- Child Class 1: SMS Service ---
class SMSNotifier(BaseNotifier):
    def __init__(self, provider_name: str, api_gateway: str):
        super().__init__(provider_name)  # Calls parent constructor
        self.api_gateway = api_gateway   # Unique attribute for SMS

    def send(self, recipient: str, message: str) -> str:
        return f"[SMS via {self.api_gateway}] Sending to {recipient}: '{message}'"


# --- Child Class 2: Email Service ---
class EmailNotifier(BaseNotifier):
    def __init__(self, provider_name: str, smtp_server: str):
        super().__init__(provider_name)  # Calls parent constructor
        self.smtp_server = smtp_server   # Unique attribute for Email

    def send(self, recipient: str, message: str) -> str:
        return f"[Email via {self.smtp_server}] Sending to {recipient}: '{message}'"