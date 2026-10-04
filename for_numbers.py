"""
example to using for loop with range number
input start stop and jump and print all numbers in range
if start bigger then stop print from start until stop with jump
if stop bigger then start print from stop until start with -jump
"""

start = int(input("please enter start number:"))
stop = int(input("please enter stop number:"))
jump = int(input("please enter jump number:"))
if start > stop:
    for i in range(start, stop, -jump):
        print(i, end=",")
    print()
elif start < stop:
    for i in range(start, stop, jump):
        print(i, end=",")
    print()
