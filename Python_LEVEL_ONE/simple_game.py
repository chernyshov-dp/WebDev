import random


def get_guess():
    return input("What is your guess?\n")


def generate_code():
    return str(random.randint(100, 999))


def generate_clues(user_guess, code):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if not clues:
        return ["nope"]
    else:
        return clues


print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!\n"
      "Close: You've guessed a correct number in the wrong position\n"
      "Match: You've guessed a correct number in the correct position\n"
      "Nope: You haven't guess any of the numbers correctly\n"
      "Code has been generated, please guess a 3 digit number")

secret_code = generate_code()
clue_report = []
print(secret_code)

while clue_report != "CODE CRACKED!":
    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
