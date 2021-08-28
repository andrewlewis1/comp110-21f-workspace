# This program shows how the four numerical operators work in Python
__author__ = "730384041"


left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
left = int(left)
right = int(right)
print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))