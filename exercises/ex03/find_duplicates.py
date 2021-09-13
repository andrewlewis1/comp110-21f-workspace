"""Finding duplicate letters in a word."""

__author__ = "730384041"

word: str = input("Enter a word: ")
i: int = 0
dup: bool = False

while i < len(word):
    char: str = word[i]
    j: int = i + 1
    while j < len(word):
        if char == word[j]:
            dup = True
        j += 1
    i += 1

print("Found duplicate: " + str(dup))