import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Number Guessing Game")
    print("Guess a number between 1 and 100\n")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too Low! Try again.\n")
        elif guess > number:
            print("Too High! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()
