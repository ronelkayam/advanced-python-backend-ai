"""
This file is review about conditions part
"""
age = (int(input("please enter your age:")))
if age > 18:
    print("Condition are True!")
print("This happen any way!")
city = input("please enter your city:")
if city == "Los Angeles":
    print("You are living in angeles city")
else:
    print("You are not living in angeles city")
print("This happen any way!")
python_grade = float(input("please enter your Python grade:"))
if python_grade == 100:
    print("You are excellent")
elif python_grade == 90:
    print("You are good student!")
elif python_grade == 80:
    print("Good grade!")
else:
    print("You should be better!")
print("This happen any way!")

if 18 < age < 30:
    print("You are young, drink beer!")
elif age > 30 or age < 50:
    print("You are cool, drink wine!")



