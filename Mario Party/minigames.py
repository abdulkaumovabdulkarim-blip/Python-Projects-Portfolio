# minigames.py

import random
import time
from classes import Player

def browsersRoulette(player, computer_player):
    random_number_explosion = random.randint(1, 10)

    exploded = True
    chosen_numbers = []

    while exploded == True:
        computer_choice = random.randint(1, 10)
        while computer_choice in chosen_numbers:
            computer_choice = random.randint(1, 10)

        print(f"Bowser Jr has choosen {computer_choice}")
        choice =input("Please select a number between 1 and 10: ")

        try:
            choice = int(choice)
        except ValueError:
            pass

        if isinstance(choice, int) == False or choice < 1 or choice > 10:
            print("Please select a valid number between 1 and 10.")
            continue

        if choice in chosen_numbers:
            print("This number has already been chosen. Please select a different number.")
            continue

        if computer_choice == random_number_explosion and choice == random_number_explosion:
            print(f"The explosion number was {random_number_explosion}!")
            print("\nBoth players exploded! You both lose!")
            exploded = False
        elif computer_choice == random_number_explosion:
            print(f"The explosion number was {random_number_explosion}!")
            print(f"\nBowser Jr hit the bomb! {player.name} wins the mini-game and gets +10 Coins!")
            player.coins += 10
            exploded = False
        elif choice == random_number_explosion:
            print(f"The explosion number was {random_number_explosion}!")
            print(f"\n{player.name} hit the bomb! Bowser Jr wins the mini-game and gets +10 Coins!")
            computer_player.coins += 10
            exploded = False
        else:
            print("\nNo one exploded! Try again!")
            chosen_numbers.append(choice)
            chosen_numbers.append(computer_choice)
            time.sleep(1)


def coinRush(player, computer_player):
    print("\n--- Press ENTER when timer ends ---")
    
    # 1. Timer
    for i in range(3, 0, -1):
        print(f"\rPress after: {i} second(s).", end="")
        time.sleep(1)
    
    print("\rPRESS ENTER!") 
    
    start_time = time.time()
    
    bot_reaction_time = round(random.uniform(0.25, 0.85), 3)
    
    input() 
    
    # Фиксируем время, когда игрок нажал Enter
    player_reaction_time = round(time.time() - start_time, 3)
    
    # 3. Сравнение результатов
    print(f"\nYour reaction time: {player_reaction_time} sec.")
    print(f"Computer's reaction time: {bot_reaction_time} sec.")
    
    if player_reaction_time < bot_reaction_time:
        print("🎉 You won +3 Coins! You were faster than the computer!")
        player.coins += 3
    else:
        print("🤖 The computer won +3 Coins! You were too slow.")
        computer_player.coins += 3





