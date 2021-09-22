"""Project 00 - Create your own adventure!"""

import random
__author__ = "730384041"
player: str
confetti = "\U0001F389"
points: int = 0


def main() -> None:
    """This is the function which serves as the entrypoint to the adventure program."""
    repeats: int = int(input("How many times would you like to go on an adventure? "))
    i: int = 0
    
    while i < repeats:
        greet()
        global points
        extremitypts: int = 0
        if level() == "peaceful":
            points += 1
            extremitypts += 1
        elif level() == "extreme":
            points += 2
            extremitypts += 2

        direction: int = path()

        if direction == 2:
            points = points + left(extremitypts)
        if direction == 3:
            points = points + right(extremitypts)
        if direction == 1:
            points = points + middle(extremitypts)

        print(f"You accumulated {points} points from this adventure! {confetti}")
        print(f"Your total number of points is {points}")
        i += 1


def greet() -> None:
    """This is the procedure for greeting the player."""
    player: str = input("What is your name? ")
    print(f"Hello {player}, welcome to this fun adventure!")


def level() -> str:
    """This is the procedure for determining the level of extremity for the adventure."""
    extremity: str = input("Would you like your adventure to be peaceful or extreme? ")
    
    return extremity


def path() -> int:
    """This is the procedure used to assign point values for path choice."""
    global points
    direction: str = input("Would you like to go down the left, right, or middle path? ")
    if direction == "left":
        points += 2
    if direction == "right":
        points += 3
    if direction == "middle":
        points += 1
    
    return points


def left(x: int) -> int:
    """This is the function used to assign point values for adventures down the left path."""
    points: int = 0
    number: int = random.randint(3, 7)
    print("You have chosen the left path!")
    if x == 1:
        print("You are hiking through the woods on a beautiful spring day.")
        print(f"As you are walking, you spot {number} deer next to you on the trail.")
        choice: str = input("Do you stop and observe them or ignore them and finish your adventure? ")
        if choice == "stop and observe them":
            points += 1
    if x == 2:
        print("You are trekking through the snow-covered woods on a harsh winter day.")
        print(f"As you are traveling, you spot a pack of {number} wolves ahead of you on the trail.")
        choice = input("Do you stand your ground or run away and end your adventure? ")
        if choice == "stand my ground":
            points += 3

    return points


def right(x: int) -> int:
    """This is the function used to assign point values for adventures down the right path."""
    points: int = 0
    number: int = random.randint(3, 7)
    print("You have chosen the right path!")
    if x == 1:
        print("You are swimming in calm seas on a beautiful summer day.")
        print(f"As you are swimming, you spot {number} dolphins next to you in the water.")
        choice: str = input("Do you stop and observe them or ignore them and finish your adventure? ")
        if choice == "stop and observe them":
            points += 1
    if x == 2:
        print("You are swimming in rough seas on a harsh winter day.")
        print(f"As you are swimming, you notice {number} sharks are beginning to circle you.")
        choice = input("Do you stand your ground or swim away and end your adventure? ")
        if choice == "stand my ground":
            points += 4

    return points


def middle(x: int) -> int:
    """This is the function used to assign point values for adventures down the middle path."""
    points: int = 0
    number: int = random.randint(3, 7)
    print("You have chosen the middle path!")
    if x == 1:
        print("You are walking down a busy city street on a nice warm day.")
        print(f"During your walk, you notice a group of {number} musicians playing at a street corner.")
        choice: str = input("Do you stop and listen or ignore them and finish your adventure? ")
        if choice == "stop and listen":
            points += 1
    if x == 2:
        print("You are walking down a deserted city street on a harsh winter night.")
        print(f"As you are walking, you notice a group of {number} people approaching you.")
        choice = input("Do you stand your ground or run away and end your adventure? ")
        if choice == "stand my ground":
            points += 2

    return points


if __name__ == "__main__":
    main()