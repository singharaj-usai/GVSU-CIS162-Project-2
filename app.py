# Project 2 hints

# roll 2 dice and accumulate points

# stop before rolling a 1 and keep points

# roll a 1, lose points from this turn

# Roll double 1s, lose all points

import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2