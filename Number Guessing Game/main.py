# main.py
# PYTHON PROJECTS - "NUMBER GUESSING GAME"

# Abdulqayumov Abdukarim

import random
import string

number_of_att = 0
def game_process(attempt, board):

    # Get random number
    number = random.randint(1, board)
    # Get user guess
    while True:
        guess = input("\nEnter your guess or exit to end: ")
        number_of_att += 1

        # Exit check
        if guess.lower() == "exit":
            last_attempt = number_of_att
            number_of_att = 0
            return f"You exited! The correct answer is {number}.\nToatl Attempts: {last_attempt}"

        # Attempts left?
        if number_of_att == attempt:
            number_of_att = 0
            return f"No attempts left!\nThe correct answer is {number}"
        
        # Input Validation
        if not guess.isdigit():
            print("⚠️ Invalid input! Please enter a number.")
            continue

        # making guess as integer and not negative
        guess = int(abs(guess))
        if guess == number:
            last_attempt = number_of_att
            number_of_att = 0
            return f"> Correct! You found the number in {last_attempt} attempts!"
        
        # Giving feedback
        if guess > number:
            print(f"> Too high! Try again. ({attempt - number_of_att} attempts left)")
        if guess < number:
            print(f"> Too low! Try again. ({attempt - number_of_att} attempts left)")



# --- START ---
print("--- Welcome to the Number Guessing Game ---")
input("Press Enter to start the game> ")

# Create the loop
exit = True
board = 10
level_list = ["1", "2", "3"]
while exit:
    # Setting the level
    level = True
    while level == True:
        print("\nChoose the level:\n\n1. Easy (1-50)\n2. Medium (1-100)\n3. Hard (1-100)")
        choice = input("\nEnter the number of level (1-3)> ")
        if choice in level_list:
            level = False
        else:
            print("Invalid choice!")

    # Setting the level's board
    if choice == "1":
        board = 50
    elif choice == "2":
        board = 100
    else:
        board = 500
    
    # Set the available number of attempts
    attempt = board // 5
    print(f"\nI'm thinking of a number between 1 and {board}.")
    print(f"You have {attempt} attempts.")
    
    # Calling the function
    print(game_process(attempt, board))

    # Exiting process
    exit_input = input("\nWould you like to play again? (y/n): ")
    if exit_input.lower() == "n":
        exit = False


# Thanks
print("\nThanks for playing!")