# Project 2 hints

# roll 2 dice and accumulate points

# stop before rolling a 1 and keep points

# roll a 1, lose points from this turn

# Roll double 1s, lose all points

import random
# Step 1
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

# step 2

def computerTurn(game_score, goal):
    turnTotal = 0
    while True:
        dice1, dice2 = roll_dice()
        print(f"computer rolled {dice1}, {dice2} turn total: {turnTotal}")

if __name__ == "__main__":
    print(roll_dice())