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
# computer_turn(game_score, goal) - performs the computer’s turn. Computer is provided a goal to achieve and then stop rolling for the current turn.
def computerTurn(game_score, goal):
    # Turn total starts at zero.
    turnTotal = 0
    while True:
        dice1, dice2 = roll_dice()
        print(f"computer rolled {dice1}, {dice2} turn total: {turnTotal}")

        # If a single 1 is rolled, set the current turn score to zero and end the turn.
        if dice1 == 1 or dice2 == 1:
            return game_score


if __name__ == "__main__":
    print(roll_dice())