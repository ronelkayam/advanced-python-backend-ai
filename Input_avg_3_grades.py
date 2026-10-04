"""
this script input 3 grades ang output avg
if avg upper 80 printing wow too
"""
java = int(input("please enter your java grade:"))
python = int(input("please enter your python grade:"))
devops = int(input("please enter your devops grade:"))
avg = (java + python + devops) / 3
print(f"Your average is {avg}")
if avg >= 80:
    print("WOOW, avg is upper then 80")
else:
    print("good job but avg is lower then 80")
