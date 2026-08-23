# main.py
# PYTHON PROJECTS - "Mario Party"

# Abdulqayumov Abdukarim

import random
from classes import Player
from logic import how_many_rounds, select_player, roll_dice, ranking
from minigames import browsersRoulette, coinRush


# --- START ---
print("--- WELCOME TO MARIO PARTY PYTHON ---")

exit = True
while exit:
    rounds = how_many_rounds()
    player1_name = select_player()
    player1 = Player(player1_name)
    print("Player 2 (Computer) is Bowser Jr.")
    computer_player = Player("Bowser Jr.")

    current_round = 1
    while current_round <= rounds:
        print(f"\n=== ROUND {current_round} START ===")
        roll_dice(player1)
        roll_dice(computer_player)

        random_game = random.randint(1, 2)
        if random_game == 1:
            print(f"\n=== ROUND {current_round} MINI-GAME: Bowser's Roulette ===")
            browsersRoulette(player1, computer_player)
        else:
            print(f"\n=== ROUND {current_round} MINI-GAME: Coin Rush ===")
            coinRush(player1, computer_player)

        if current_round == rounds:
            print("\n--- FINAL STANDINGS ---")
            if player1.coins > computer_player.coins:
                print(f"WINNER: {player1.name}")
                print(f"Final Stats: {player1.name} ({player1.coins} Coins, {player1.stars} Stars)")
            elif computer_player.coins > player1.coins:
                print(f"WINNER: {computer_player.name}")
                print(f"Final Stats: {computer_player.name} ({computer_player.coins} Coins, {computer_player.stars} Stars)")
            else:
                print(f"WINNERS: {player1.name} and {computer_player.name} (TIE)")
                print(f"Final Stats: {player1.name} ({player1.coins} Coins, {player1.stars} Stars) and {computer_player.name} ({computer_player.coins} Coins, {computer_player.stars} Stars)")
        else:
            print(f"\n--- ROUND {current_round} STANDINGS ---")
            ranking(player1, computer_player)


        current_round += 1


    exit_choice = input("\nDo you want to play again? (yes/no): ")
    if exit_choice.lower() != "yes":
        exit = False
        print("\n--- GAME OVER ---")
    else:
        print("\n--- Starting a new game ---")

print("Thank you for playing Mario Party Python!")
