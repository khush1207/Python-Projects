import random
from words import word_list
from art import logo, stages

# Choosing a random word from word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
display = ['_' for _ in range(word_length)]
guessed_letters = []

print(logo)

game_over = False
while not game_over:
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'. Try again!")
        continue
    guessed_letters.append(guess)

    # Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(stages[lives])
        print(f"'{guess}' is not in the word. You lose a life!")
        print(f"Lives left {lives}")

    # Check game end conditions
    if "_" not in display:
        print(chosen_word)
        print("Congratulations! You guessed the word correctly!")
        game_over = True
    elif lives == 0:
        print("Game Over! The word was:", chosen_word)
        game_over = True
