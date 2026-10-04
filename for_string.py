"""
example to using for loop with string range
input string and count !,#,%,$ chars appears at string
"""

str_to_test = input("please enter string:")
count = 0
for char in str_to_test:
    if char == '!' or char == '#' or char == '%' or char == '$':
        count += 1
print(f"count of specials chars:{count}")
