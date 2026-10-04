"""
mail validation ex.
input mail address and return if legal or illegal
to be legal  - @ appears 1 time and . appears 2 times
all other cases mail address are illegal
* efficiency!!
"""
mail_address = input("please enter mail address:")
at_count = 0
dot_count = 0
for char in mail_address:
    if char =='@':
        at_count+=1
    elif char =='.':
        dot_count+=1
if at_count==1 and dot_count==2:
    print(f"{mail_address} is legal")
else:
    print(f"{mail_address} is illegal")