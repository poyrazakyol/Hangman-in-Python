import random
from wordlist import words

def get_word(words):
    word = random.choice(words)
    return word.upper()

correct_letter = ""

word = get_word(words)
count = 6

while count > 0:
    guess = input(" Enter a letter: ")
    if (guess.isalpha() == 0 or guess != type(chr) or len(guess) != 1):
        print("Please enter Alphabetic character!")
        continue

    if guess in word:
        print(f"Good job! There is one or more {guess} in the word.")
    else:
        count -= 1
        print(f"Wrong answer. There is no {guess} in the word. {count} turn(s) left.")

    correct_letter += guess
    wrong = 0

    for letter in word:
        if letter in correct_letter:
            print(f"{letter}",end="")
        else:
            print("_",end="")
            wrong += 1

    if wrong == 0:
        print(f" Congrats! The word was: {word}.")
        break
else:
    print("Sorry, You didn't win!")                    