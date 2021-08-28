# This program demonstrates how four relational operators work in Python
__author__ = "730384041"


left : str = input("Left-hand side: ")
right : str = input("Left-hand side: ")
left : int(left)
right : int(right)

if left < right:
    print(str(left) + " < " + str(right) + " is True")
else:
    print(str(left) + " < " + str(right) + " is False")

if left >= right:
    print(str(left) + " >= " + str(right) + " is True")
else:
    print(str(left) + " >= " + str(right) + " is False")

if left == right:
    print(str(left) + " == " + str(right) + " is True")
else:
    print(str(left) + " == " + str(right) + " is False")

if left != right:
    print(str(left) + " != " + str(right) + " is True")
else:
    print(str(left) + " != " + str(right) + " is False")
