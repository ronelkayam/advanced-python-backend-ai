# ==============================================================================
# PYTHON LISTS: 20 EXERCISES & SOLUTIONS
# Instructor: DevOps Course Materials
# Description: This file contains 20 progressive exercises on Python lists,
# complete with comments describing the tasks and fully working solutions.
# ==============================================================================


# ------------------------------------------------------------------------------
# EXERCISE 1: Creation and Indexing
# Task: Create a list named 'colors' containing at least 4 colors. 
# Print the first color and the last color (using negative indexing).
# ------------------------------------------------------------------------------
# Solution 1:
colors = ["red", "blue", "green", "yellow"]
print("First color:", colors[0])
print("Last color:", colors[-1])


# ------------------------------------------------------------------------------
# EXERCISE 2: Modifying Elements
# Task: Create a list of three animals: ["cat", "dog", "rabbit"]. 
# Change the second element ("dog") to "hamster", and print the updated list.
# ------------------------------------------------------------------------------
# Solution 2:
animals = ["cat", "dog", "rabbit"]
animals[1] = "hamster"
print("Updated animals list:", animals)


# ------------------------------------------------------------------------------
# EXERCISE 3: Checking Length
# Task: Write a program that takes a list of numbers, checks how many elements 
# it contains using len(), and prints a descriptive message.
# ------------------------------------------------------------------------------
# Solution 3:
numbers = [10, 20, 30, 40, 50]
list_length = len(numbers)
print(f"This list contains {list_length} elements.")


# ------------------------------------------------------------------------------
# EXERCISE 4: List Concatenation
# Task: Create two lists of numbers, combine them using the '+' operator 
# into a single new list, and print the result.
# ------------------------------------------------------------------------------
# Solution 4:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined list:", combined_list)


# ------------------------------------------------------------------------------
# EXERCISE 5: List Multiplication
# Task: Create a list containing a single string ["Python"], multiply it by 5, 
# and print the result.
# ------------------------------------------------------------------------------
# Solution 5:
single_item_list = ["Python"]
multiplied_list = single_item_list * 5
print("Multiplied list:", multiplied_list)


# ------------------------------------------------------------------------------
# EXERCISE 6: Basic Addition and Removal (append & remove)
# Task: Create an empty list named 'shopping_list'. Add 3 items using append(). 
# Then, remove the second item using remove() and print the final list.
# ------------------------------------------------------------------------------
# Solution 6:
shopping_list = []
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.remove("bread")
print("Shopping list:", shopping_list)


# ------------------------------------------------------------------------------
# EXERCISE 7: Using Pop
# Task: Create a list of numbers: [10, 20, 30, 40]. Use pop() to remove the 
# last item, store it in a variable, and print both the updated list and the popped item.
# ------------------------------------------------------------------------------
# Solution 7:
nums = [10, 20, 30, 40]
popped_item = nums.pop()
print("List after pop:", nums)
print("Popped item:", popped_item)


# ------------------------------------------------------------------------------
# EXERCISE 8: Using Insert
# Task: Create a list with 3 names. Use insert() to add a new name precisely 
# at the second position (index 1), and print the list.
# ------------------------------------------------------------------------------
# Solution 8:
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print("Names list after insert:", names)


# ------------------------------------------------------------------------------
# EXERCISE 9: Clear a List
# Task: Create a list with several items, apply the clear() method to it, 
# and print it to verify it is completely empty.
# ------------------------------------------------------------------------------
# Solution 9:
server_logs = ["error", "warning", "info"]
server_logs.clear()
print("Cleared logs list:", server_logs)


# ------------------------------------------------------------------------------
# EXERCISE 10: Checking Membership (in)
# Task: Create a list of foods. Write code that checks using the 'in' operator 
# whether the word "pizza" is in the list and prints an appropriate message.
# ------------------------------------------------------------------------------
# Solution 10:
foods = ["apple", "burger", "pizza", "sushi"]
if "pizza" in foods:
    print("Pizza is in the food list!")
else:
    print("Pizza is not in the list.")


# ------------------------------------------------------------------------------
# EXERCISE 11: List Slicing
# Task: Given a list nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], extract only the 
# three middle elements (4, 5, 6) using slicing and print them.
# ------------------------------------------------------------------------------
# Solution 11:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle_elements = nums[3:6]
print("Middle elements:", middle_elements)


# ------------------------------------------------------------------------------
# EXERCISE 12: Reversing a List with Slicing
# Task: Use the slicing step technique ([::-1]) to reverse a given list of numbers 
# and print the result.
# ------------------------------------------------------------------------------
# Solution 12:
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print("Reversed list:", reversed_list)


# ------------------------------------------------------------------------------
# EXERCISE 13: Difference Between sort() and sorted()
# Task: Create an unsorted list: scores = [85, 90, 70, 95]. Use sorted() to create 
# a new sorted list copy, and print both to prove the original didn't change.
# ------------------------------------------------------------------------------
# Solution 13:
scores = [85, 90, 70, 95]
sorted_scores = sorted(scores)
print("Original scores (unchanged):", scores)
print("New sorted scores:", sorted_scores)


# ------------------------------------------------------------------------------
# EXERCISE 14: In-place Sorting and Reversing
# Task: Create an unsorted list of numbers, sort it in ascending order using 
# sort(), and then reverse its order using the reverse() method.
# ------------------------------------------------------------------------------
# Solution 14:
numbers_list = [42, 12, 99, 5, 23]
numbers_list.sort()
print("Sorted ascending:", numbers_list)
numbers_list.reverse()
print("Reversed order:", numbers_list)


# ------------------------------------------------------------------------------
# EXERCISE 15: Summing Elements via Loop
# Task: Create a list of numbers. Write a for loop that iterates through the list, 
# calculates their total sum, and prints it (without using the built-in sum() function).
# ------------------------------------------------------------------------------
# Solution 15:
values = [10, 20, 30, 40]
total_sum = 0
for val in values:
    total_sum += val
print("Total sum via loop:", total_sum)


# ------------------------------------------------------------------------------
# EXERCISE 16: Finding Maximum Value Manually
# Task: Create a list of numbers. Write code using a loop to find the highest value 
# in the list without using the built-in max() function, then print it.
# ------------------------------------------------------------------------------
# Solution 16:
numbers_set = [15, 42, 7, 89, 23]
highest = numbers_set[0]
for num in numbers_set:
    if num > highest:
        highest = num
print("Highest value found manually:", highest)


# ------------------------------------------------------------------------------
# EXERCISE 17: Counting Occurrences (count)
# Task: Create a list where a specific element appears multiple times. 
# Use the count() method to discover how many times it appears and print the result.
# ------------------------------------------------------------------------------
# Solution 17:
letters = ['a', 'b', 'a', 'c', 'a', 'd']
count_a = letters.count('a')
print("The letter 'a' appears times:", count_a)


# ------------------------------------------------------------------------------
# EXERCISE 18: Finding Index of a Value (index)
# Task: Create a list of city names. Use the index() method to find the index 
# position of a specific city and print its location.
# ------------------------------------------------------------------------------
# Solution 18:
cities = ["New York", "London", "Tokyo", "Paris"]
tokyo_index = cities.index("Tokyo")
print("Tokyo is located at index:", tokyo_index)


# ------------------------------------------------------------------------------
# EXERCISE 19: Filtering Even Numbers (List Comprehension)
# Task: Given numbers = [1, 2, 3, 4, 5, 6, 7, 8], use a List Comprehension 
# to create a new list containing only the even numbers, and print it.
# ------------------------------------------------------------------------------
# Solution 19:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers filtered:", even_numbers)


# ------------------------------------------------------------------------------
# EXERCISE 20: Generating Squares (List Comprehension)
# Task: Use a List Comprehension and range() to create a list of squared numbers 
# from 1 to 10 (i.e., [1, 4, 9, ..., 100]) and print the resulting list.
# ------------------------------------------------------------------------------
# Solution 20:
squares = [x ** 2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)