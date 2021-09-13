"""An exercise in remainders and boolean logic."""

__author__ = "730384041"

# Begin your solution here...
n: int = int(input("Enter an int: "))

if n % 2 == 0 and n % 7 == 0:
    print("TAR HEELS")
elif n % 2 == 0:
    print("TAR")
elif n % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")