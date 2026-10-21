"""
===================================================================
 Topic: Object-Oriented Programming (OOP) - Comprehensive Integration
 File: main.py (Notification System Execution)
===================================================================

Description:
This file serves as the execution entry point for our notification system,
combining all major OOP principles across multiple modules:
1. Encapsulation: Testing private attributes and protected updates via setters.
2. Inheritance: Utilizing specialized notifier classes inheriting from a base class.
3. Polymorphism / Duck Typing: Using a generic `execute_notifications` function
   that works seamlessly with both Email and SMS services.

Requirements to run:
- Make sure `oop_final_exe_models_notifications_system.py` and `oop_final_exe_services_notifications_system.py`
  are saved in the same directory!
"""

from oop_final_exe_models_notifications_system import User
from oop_final_exe_services_notifications_system import EmailNotifier, SMSNotifier

print("---- Starting Notification System Test -----")

# Polymorphic helper function - accepts any notifier object that implements
# log_delivery() and send() methods.
def execute_notifications(notifier, recipient: str, message: str):
    print(notifier.log_delivery())
    result = notifier.send(recipient, message)
    print(result)
    print("-" * 40)


# --- Program Execution / Example Usage ---

# 1. Instantiating a User object (from models module)
u1 = User("dana_dev", "dana@example.com", "050-111111")
print(f"User created: {u1.user_name}")

# 2. Testing Encapsulation: updating email with invalid vs valid values
print("\n--- Testing Email Updates (Encapsulation Validation) ---")
u1.set_email("invalid-email-no-at-sign")
u1.set_email("dana.new@gmail.com")

# 3. Testing private attribute access restriction (Name Mangling)
print("\n--- Testing Private Attribute Access ---")
try:
    # Trying to access a private attribute directly will trigger an AttributeError
    print(u1.__email)
except AttributeError:
    print("Access denied! Private attributes cannot be accessed directly from outside.")

# 4. Creating service objects (from services module using Inheritance)
email_service = EmailNotifier("SendGrid", "smtp.sendgrid.net")
sms_service = SMSNotifier("Twilio", "api.twilio.com")

# 5. Testing Polymorphism: executing the same function with different service objects
print("\n----- Sending System Alerts (Polymorphism) -------")
execute_notifications(email_service, u1.get_email(), "Welcome to our backend platform!")
execute_notifications(sms_service, u1.get_phone_number(), "Your verification code is: 3589")