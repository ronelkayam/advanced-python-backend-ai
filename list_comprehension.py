"""
list comprehension it's shortly and elegant way
to create new lists on base exists lists in python
3/2 parts - first - what put inside the new list
second - what the exists range/list
third - optional - condition on exists range
"""

# create list of power numbers (1-5)
squares = [x ** 2 for x in range(1, 6)]
print(f"[x ** 2 for x in range(1, 6)]->{squares}")  # [1,4,9,16,25]

# list by filtering - only even numbers by exists list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"x for x in numbers if x % 2 == 0->{evens}")#[2,4,6,8,10]
