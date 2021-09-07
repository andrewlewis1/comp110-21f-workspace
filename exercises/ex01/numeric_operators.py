"""This program shows how the four numerical operators work in Python."""
__author__ = "730384041"


left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
left1 = int(left)
right1 = int(right)
print(str(left) + " ** " + str(right) + " is " + str(left1 ** right1))
print(str(left) + " / " + str(right) + " is " + str(left1 / right1))
print(str(left) + " // " + str(right) + " is " + str(left1 // right1))
print(str(left) + " % " + str(right) + " is " + str(left1 % right1))