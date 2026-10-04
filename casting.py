"""
Casting means converting a value from
one data type to another.
I can test with type() function
"""
# converts the string "5" into integer 5
num = int("5")
print(num)
print(type(num))

#converts input
num = int(input("please enter a number:"))
print(num)
print(type(num))

#converts to float type
float_num = float(input("please enter a number:"))
print(float_num)
print(type(float_num))

#converts back to str type
str_num = str(float_num)
print(str_num)
print(type(str_num))


#converts int to float
int_num = 23
print(int_num)
print(type(int_num))
float_num = float(int_num)
print(float_num)
print(type(float_num))

#converts float to int
float_num = 234.24423
print(float_num)
print(type(float_num))
int_num = int(float_num)
print(int_num)
print(type(int_num))