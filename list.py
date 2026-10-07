"""
This file is short tutorial about list in python
first location in list = 0
last location - ls.length -1
it's possible to mix variables in same list
"""

# create new list
empty_list = []  # empty list
list_with_same_values = [1, 2, 3, 4]
list_with_same_values1 = [True, False, False, True]
list_with_mix_values_type = [1, True, 2.343, -3432.45, "hello python"]
print("****initialize lists*****")
print(f"empty list ->{empty_list}")
print(f"list with same values boolean->{list_with_same_values1}")
print(f"list with mix values type->{list_with_mix_values_type}")

# append(item) - >adding new value in last position
print("\n\n**********append function*********")
print(f"list before adding with append()-> {list_with_mix_values_type}")
list_with_mix_values_type.append(3)
print(f"list after append()-> {list_with_mix_values_type}")

# list length
print("\n\n***********length function************")
print(f"list ->{list_with_same_values} length ->{len(list_with_same_values)}")

# insert(index,item) - add item in specific index
print("\n\n**********insert function**************")
print(f"list before insert->{list_with_same_values}")
list_with_same_values.insert(2, "new value by insert")
print(f"list after insert->{list_with_same_values}")

# best practice
print("\n\n**********insert function best practice************")
index = 5
if len(list_with_mix_values_type) > index:
    list_with_same_values.insert(index, "new value by insert")
    print(f"insert success->{list_with_same_values}")
else:
    print(f"insert fail->{list_with_mix_values_type}")

# remove(value) -> remove specific value only first appears
print("\n\n**********remove by value ************")
print(f"list before remove->{list_with_mix_values_type}")
value_to_remove = 2.343
list_with_mix_values_type.remove(value_to_remove)
print(f"removing {value_to_remove} success")
print(f"list after remove->{list_with_mix_values_type}")

# remove by index del ls_name[index_to_remove]
print("\n\n**********remove by index best practice *************")
index_to_remove = 100
print(f"list before remove -{list_with_mix_values_type}")
if len(list_with_mix_values_type) > index_to_remove:
    del list_with_mix_values_type[index_to_remove]
    print(f"remove success->{list_with_mix_values_type}")
else:
    print(f"remove fail->{list_with_mix_values_type}")

"""
sort vs sorted
sort - function that belong to list class, change the original list
sorted - building function,get any list create copy sort the copy list and returned
"""
numbers = [34, 5, 76, 4, 7, 89]
print(f"\n\n list before all->{numbers}")
print("\n\n*******sort by sorted func*******")
sorted_ls = sorted(numbers)
print(f"original list after sorted function->{numbers}\nsorted list->{sorted_ls}\n")
print("\n\n*******sort by sort func*******")
numbers.sort()
print(f"original list after sort function->{numbers}\n")

# get specific value by index - should to ensure that index are exists in list
print("\n\n********getting values in list******")
fruits = ['apple', 'banana', 'cherry', 'watermelon', 'avocado', 'mango']
print(f"second location value getting by ls_name[index]->{fruits[1]}")
# negative index counting from end
print(f"last location value getting by fruits[-1]->{fruits[-1]}")
# another option to get last value in list
print(f"last value in list getting by fruits[len(fruits)-1]->{fruits[len(fruits) - 1]}")

# slicing - possible to get part from list by slicing [start:and] ,start included, end not included
colors = ['red', 'blue', 'brown', 'white', 'yellow', 'purple', 'black', 'green']
sub_colors = colors[1:4]
print(f"colors[1:4]->sub_colors")  # ['blue','brown','white']
sub_colors1 = colors[1:5:2]
print(f"colors[1:5:2]->{sub_colors1}")  # ['blue','white']
sub_colors2 = colors[:3]
print(f"colors[:3]->{sub_colors2}")  # ['red','blue','brown']

# Iterating through a list
print("\n\n************Iterating through a list****************")
cars_ls = ['BMW', 'mazda', 'toyota', 'mercedes', 'audi', 'subaro']
for car in cars_ls:
    print(car)

"""
exercise - 
input 10 grades
output max and min grade
using in loops only!
"""
grades = []
length = 10
for i in range(length):
    grades.append(int(input("Enter grade: ")))

print(f"grades list->{grades}")
max_grade = grades[0]
min_grades = grades[0]
for grade in range(1, length):
    if grades[grade] > max_grade:
        max_grade = grades[grade]
    elif grades[grade] < min_grades:
        min_grades = grades[grade]
print(f"max grade->{max_grade}")
print(f"min grade->{min_grades}")