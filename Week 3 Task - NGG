#!/usr/bin/env python3
# coding: utf-8

import random  # Import random module for generating random numbers


def play_game(n_max: int):
    """Handle the main guessing process of the game."""
    secret = random.randint(1, n_max)
    guess_count = 0

    while True:
        guess = input(f"Guess the number (1-{n_max}): ")
        if guess.isdigit():
            guess = int(guess)
            guess_count += 1
            if guess == secret:
                print(f"You got it in {guess_count} guesses!")
                break
            elif guess > secret:
                print("Too high. Guess again.")
            else:
                print("Too low. Guess again.")
        else:
            print("Please enter a valid integer.")


# The game starts here
print("Let's play Guess the Number.")

# The main game loop
while True:
    # Set the initial difficulty level to 0
    difficulty = 0

    # Loop to ensure a valid difficulty level is chosen
    while True:
        # Prompt user to pick a difficulty level
        difficulty = input("Pick a difficulty level (1, 2, or 3): ")

        # Check if input is a digit and within the valid range
        if difficulty.isdigit() and 1 <= int(difficulty) <= 3:
            difficulty = int(difficulty)  # Convert string input to integer
            break  # Exit loop if valid input is provided
        else:
            print("Please enter 1, 2, or 3.")  # Prompt for valid input

    # Assign a maximum number for guessing based on the chosen difficulty
    n_max = 10
    if difficulty == 2:
        n_max = 100
    elif difficulty == 3:
        n_max = 1000

    play_game(n_max)  # Call the play_game function

    # Ask user if they want to play again
    play_again = input("Do you want to play again (y/N)? ")

    # Convert input to lowercase and remove leading/trailing spaces
    play_again = play_again.lower().strip()

    # Check if the response starts with 'n' ('no', 'nope', 'nah', 'negative', 'never again')
    if play_again.startswith("n"):
        break  # Exit the main game loop if user chooses not to play again
