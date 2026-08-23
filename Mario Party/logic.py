# logic.py

import random
import time
from classes import Space

# Ask how many rounds to play
def how_many_rounds():
    while True:
        choice = input("How many rounds would you like to play? ")
        try:
            rounds = int(choice)
            if rounds > 0:
                return rounds
            print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Select player character
def select_player():
    while True:
        player_name = input("Player 1, select your character (Mario/Luigi/Peach): ").strip().capitalize()
        if player_name in ["Mario", "Luigi", "Peach"]:
            return player_name
        print("Invalid choice! Choose Mario, Luigi, or Peach.")

# Let's roll the dice and move the player
def roll_dice(player):
    print(f"\n--- {player.name} Turn ---")

    is_player_computer = player.name == "Bowser Jr."
    space = random.randint(1, 10)

    time.sleep(1)

    print(f"{player.name} rolls a {space}! (Moved from {player.current_board_position} to {player.current_board_position + space})")
    player.current_board_position += space
    time.sleep(1)

    space = Space(player.current_board_position)
    space_type_string = f"{player.name} landed on a {player.current_board_position}!"

    if space.space_type == "Star Space":
        print(space_type_string)
        if is_player_computer:
            if player.coins >= 20:
                player.coins -= 20
                player.stars += 1
                print(f"{player.name} bought a star!")
            else:
                print(f"Not enough coins!")
        else:
            choice = input("Do you want to buy a star for 20 coins? (yes/no): ")
            if choice.lower() == "yes":
                if player.coins >= 20:
                    player.coins -= 20
                    player.stars += 1
                    print(f"{player.name} bought a star!")
                else:
                    print("Not enough coins!")
    elif space.space_type == "Blue Space":
        space_type_string += " +3 coins."
        print(space_type_string)
        player.coins += 3
    elif space.space_type == "Red Space":
        space_type_string += " -3 coins."
        print(space_type_string)
        if player.coins >= 3:
           player.coins -= 3
        elif (player.coins < 3 and player.coins > 0) or player.coins == 0:
            player.coins = 0
    elif space.space_type == "Bowser Space":
        space_type_string += " Lose half coins."
        print(space_type_string)
        player.coins = player.coins // 2
    time.sleep(1)

    print(f"Current Stats: {player.name} ({player.coins} Coins, {player.stars} Stars)")
    time.sleep(1)

# Ranking players based on their current board position
def ranking(player1, computer_player):

    if player1.stars == computer_player.stars:
        top_player = player1 if player1.coins >= computer_player.coins else computer_player
        second_player = computer_player if top_player == player1 else player1
    elif player1.stars > computer_player.stars:
        top_player = player1
        second_player = computer_player
    else:
        top_player = computer_player
        second_player = player1

    print(f"1st: {top_player.name} ({top_player.coins} Coins, {top_player.stars} Stars)")
    print(f"2nd: {second_player.name} ({second_player.coins} Coins, {second_player.stars} Stars)")
    time.sleep(1)