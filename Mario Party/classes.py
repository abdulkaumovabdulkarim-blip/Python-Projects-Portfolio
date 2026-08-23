#logic.py
import random 

class Player:
    def __init__(self, name):
        self.name = name
        self.current_board_position = 0
        self.coins = 10
        self.stars = 0

class Space:
    def __init__(self, space_number):
        self.space_number = space_number

        numbers = [10, 5, 3, 2]

        star_space_index = random.randint(0, 3)
        red_space_index = random.randint(0, 3)
        bowser_space_index = random.randint(0, 3)
        blue_space_index = random.randint(0, 3)

        if self.space_number % numbers[star_space_index] == 0:
            self.space_type = "Star Space"
        elif self.space_number % numbers[red_space_index] == 0:
            self.space_type = "Red Space"
        elif self.space_number % numbers[bowser_space_index] == 0:
            self.space_type = "Bowser Space"
        elif self.space_number % numbers[blue_space_index] == 0:
            self.space_type = "Blue Space"
        else:
            self.space_type = "Normal Space"