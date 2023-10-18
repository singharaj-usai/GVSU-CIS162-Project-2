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
def computer_turn(game_score, goal):
    # Turn total starts at zero.
    turnTotal = 0
    while True:
        dice1, dice2 = roll_dice()
        print(f"computer rolled {dice1}, {dice2} turn total: {turnTotal}")

        # If a single 1 is rolled, set the current turn score to zero and end the turn.
        if dice1 == 1 or dice2 == 1:
            return game_score

        #  If double 1s are rolled, set game_score to zero and end the turn.
        elif dice1 and dice2 == 1:
            return 0

        # add both dice to the turn score.
        # Print the rolled dice and turn score after each roll.
        # At the end of the turn, return the updated game_score.
        if turnTotal >= goal:
            game_score += turnTotal
            return game_score

        turnTotal += dice1 + dice2

if __name__ == "__main__":
    print(roll_dice())
    print(computer_turn(0, 20))