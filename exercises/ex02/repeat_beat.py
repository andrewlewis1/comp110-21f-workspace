"""Repeating a beat in a loop."""

__author__ = "730384041"

# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
beat1: str = beat
repeats: int = int(input("How many times do you want to repeat it? "))
counter: int = 1
if repeats < counter:
    print("No beat...")

while counter < repeats:
    beat = beat + " " + beat1
    counter = counter + 1

if counter == repeats:
    print(beat)