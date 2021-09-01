# This program demonstrates how four relational operators work in Python
__author__ = "730384041"


left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
left1 = int(left)
right1 = int(right)

if left1 < right1:
    print(str(left) + " < " + str(right) + " is True")
else:
    print(str(left) + " < " + str(right) + " is False")

if left1 >= right1:
    print(str(left) + " >= " + str(right) + " is True")
else:
    print(str(left) + " >= " + str(right) + " is False")

if left1 == right1:
    print(str(left) + " == " + str(right) + " is True")
else:
    print(str(left) + " == " + str(right) + " is False")

if left1 != right1:
    print(str(left) + " != " + str(right) + " is True")
else:
    print(str(left) + " != " + str(right) + " is False")
