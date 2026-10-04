"""
conditional statements (if,else,elif) allow your program
to make decisions and execute different blocks of code depending on
whether a condition is true or false.

important point to remember
indentation: in python indentation (spaces at the beginning of the line) is a critical
the inner condition must be indented further inward relative to the other condition
so python knows belongs inside it
"""
# simple if - make happen only if condition true
print("***** if case****")
age = float(input("How old are you? "))
if age >= 18:
    print("You are adult!")
print("make happen any way!")

# if else - one option if true seconde all others
print("***** if else case******")
age = float(input("How old are you? "))
if age >= 18:
    print("you are adult!")
else:
    print("You are young, no beer!")
print("make happen any way!")

# if elif - all specific case get reference
print("***** if elif case****")
age = float(input("How old are you? "))
if age == 10:
    print("You are 10 years old, drink water")
elif age == 15:
    print("You are 15 years old, drink Kola")
elif age == 20:
    print("You are adult!")
else:
    print("all options wrongs!")
print("make happen any way!")
