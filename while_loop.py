"""
While loop
our responsibility to ensure that ending
we use with this loop kind when we don't know what the end time
we should be sure the loop are ending at some point
"""
# unstopped loop
# guess = int(input("please enter your guess:"))
# while guess != 20:
#     print("Wrong guess!")
# print("Make happen any way!")

salary = int(input("please enter your salary:"))
while salary <= 20000:
    salary = int(input("Me salary is not enough, please increase!\n"))
print("Make happen any way!")

# combined loop
age = int(input("please enter your age:"))
city = input("please enter your city:")
while age < 20 or city != "Tel aviv":
    print("One condition are false\nyou must living in Tel aviv or be bigger then 20:")
    age = int(input("please enter your age:"))
    city = input("please enter your city:")
print("Make happen any way!")

# nested loop
row = 1
column = 1
while row < 11:
    while column < 11:
        print(row * column, end=" ")
        column += 1
    print()
    row += 1
    column = 1
print("Make happen any way!")
