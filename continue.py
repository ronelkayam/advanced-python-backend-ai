"""
continue using when we want to skip about specific case
using for &while loop
rum all range 1-100 and print all even numbers only
"""
for i in range(1, 101):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
print("Code comes here only when loop ending!")