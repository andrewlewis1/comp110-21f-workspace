"""Drawing forests in a loop."""

__author__ = "730384041"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
TREE1: str = TREE
depth: int = int(input("Depth: "))
i: int = 1

while i < depth:
    print(TREE)
    TREE = TREE + TREE1
    i += 1

print(TREE)