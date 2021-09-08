"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730384041"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint

# Begin your solution here...

i: int = randint(1, 4)
print("Your fortune cookie says...")
if i == 1:
    print("A beautiful, smart, and loving person will be coming into your life.")
else:
    if i == 2:
        print("A faithful friend is a strong defense.")
    else:
        if i == 3:
            print("A fresh start will put you on your way.")
        else:
            print("All will go well with your new project.")
print("Now, go spread positive vibes!")