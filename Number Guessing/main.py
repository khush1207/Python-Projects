import random


def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = 10 if difficulty == 'easy' else 4

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"Congratulations! You guessed the number {number} correctly!")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")

        attempts -= 1
        if attempts == 0:
            print(f"You've run out of attempts! The number was {number}. Game over.")
        else:
            print("Guess again.")


# Run the game
guess_number()