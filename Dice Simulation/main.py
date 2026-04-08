
import random
import time

# Dice visualization
DICE = {
    1:("---------", "|       |","|   O   |", "|       |","--------- "),
    2:("---------", "|       |","| O   O |", "|       |","--------- "),
    3:("---------", "| O     |","|   O   |", "|     O |","--------- "),
    4:("---------", "| O   O |","|       |", "| O   O |","--------- "),
    5:("---------", "| O   O |","|   O   |", "| O   O |","--------- "),
    6:("---------", "| O   O |","| O   O |", "| O   O |","--------- "),
}

dice_numbertimes = [0,0,0,0,0,0]
# Function to show the result
def roll_dice_result(dices):
    # Get random number
    sum = 0
    # Wait for rolling
    print("\nRolling... 1 Seconds")
    time.sleep(1)

    for i in range(dices):
        n = random.randint(1, 6)
        
        # Count how many times numbers showed
        dice_numbertimes[n-1] += 1
        # Add to sum
        sum += n

        print(f"Result {i+1}: [ {n} ]")
        for line in DICE[n]:
            print(line)
        
    print(f"Total sum: {sum}")


# --- START ---
print("--- Virtual Dice Roller ---")

exit = True
while exit == True:
    # How many
    while True:
        u_input = input("\nHow many dice would you like to roll? ")
        # Check for digit
        try:
            n_dices = int(u_input)
            break
        except ValueError:
            print("Invalid Input! Enter number, Try again")
    # Call function
    roll_dice_result(n_dices)

    # Ask next rolling dice
    exit_loop = input("\nWould like to roll again? [y/n]; ")
    if exit_loop.lower() == "n":
        exit = False

# Show how many times he got (1-6) numbers
print("\nHow many times each number (1-6) has appeared during the session: ")
for i in range(6):
    print(f"{i+1} appeared {dice_numbertimes[i]} times")

# Thanks
print("\nThank you. Good bye!")
#--- END ---