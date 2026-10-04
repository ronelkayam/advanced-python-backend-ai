"""
range function tutorial
range(stop)- start from 0 included until stop not included
range(start,stop) - from start included until stop not included
range(start,stop,jump)- from start included until stop not included with jumping
"""

print(f"range(5)->",list(range(5)))#0,1,2,3,4
print(f"range(2,5)->",list(range(2,5)))#2,3,4
print(f"range(4,10,2)->",list(range(4,10,2)))#4,6,8
