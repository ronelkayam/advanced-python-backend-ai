"""
break - if we want to break out of the
using while &for loops
all thing in loop are coming after break doesn't happen
input string and print chars separetly if appears ! or $ break
"""
str_to_check = input("Enter string:")
for char in str_to_check:
    if char=='!' or char =='$':
        break
    print(char)
print("code comes here after ending loop or when break happen!")



