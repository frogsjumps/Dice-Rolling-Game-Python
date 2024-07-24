## Dice rolling simulator

import random

number_of_dice = int(input("Enter the number of dice you would like: "))
number_of_rolls = int(input("Enter the number of rolls you would like: "))

def dice_rolls (number_of_dice, number_of_rolls):
    roll_number = 0
    while number_of_rolls > 0:
        y = 0
        x = 0
        roll_number += 1
        number_of_rolls -= 1
        x = x + number_of_dice
        print('')
        enter = input(f'Press enter for roll {roll_number}:')
        while x > 0:
            y = y + 1
            dice_number = random.randint(1, 6)
            print(f"dice {y} rolled: {dice_number}")
            x -= 1



dice_rolls(number_of_dice, number_of_rolls)
