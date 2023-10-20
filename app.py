# Project 2 hints

# roll 2 dice and accumulate points

# stop before rolling a 1 and keep points

# roll a 1, lose points from this turn

# Roll double 1s, lose all points

import random

def validate_response(choice):
    validate_response = [
        "Y",
        "N",
        "y",
        "n"
    ]

    if choice in validate_response:
        return True
    else:

        print("Oops! Your choice must be Y or N.")
        return False

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
    # while loop continues until the computers turn meets those if statements
    while True:
        # Store the roll_dice func with the dice1 and dice2 values
        dice1, dice2 = roll_dice()
        # Print the computer's dice roll and the total turn
        print(f"computer rolled {dice1}, {dice2} turn total: {turnTotal}")

        # If a single 1 is rolled, set the current turn score to zero and end the turn.
        if dice1 == 1 or dice2 == 1:
            print("computer rolled 1. turn score lost")
            return game_score

        #  If double 1s are rolled, set game_score to zero and end the turn.
        elif dice1 and dice2 == 1:
            print("computer rolled double 1. Game score is 0")
            return 0

        # add both dice to the turn score.
        # Print the rolled dice and turn score after each roll.
        # At the end of the turn, return the updated game_score.
        if turnTotal >= goal:
            print("Computer reached goal. Returned game score")
            # Update the game score
            game_score += turnTotal
            # return the game score
            return game_score
        # add the total turn to both of the dices
        turnTotal += dice1 + dice2

def human_turn(game_score):
    # init total score
    totalScore = 0
    while True:
        dice1, dice2 = roll_dice()
        print(f"you rolled {dice1}, {dice2} turn total: {totalScore}")
        # check if either dice is rolled 1
        if dice1 == 1 or dice2 == 1:
            # if it is, print and return the game score
            print("you rolled 1. Turn lost")
            return game_score
        # Choice prompt
        choice = input("Roll again? (y/n) ").strip().lower()
        # If player doesn't input y,
        if choice != "y":
            # add the game score to total score
            game_score += totalScore
            # and return the game score
            return game_score
        # Add the total score to both dices if player choose to roll again
        totalScore += dice1 + dice2
        #Print the updated score
        print(f"Turn total: {totalScore}")


# human_vs_computer() – supports a full game of person versus the computer.
# Play continues until someone wins with at least 100 points.
# Human goes first.
# Computer’s goal is 20 each turn.
def human_vs_computer():
    # init goal and score
    computerGoal = 20
    humanScore = 0
    computerScore = 0

    # Play continues until someone wins with at least 100 points
    # Print the current score for each player (see sample output).
    while humanScore < 100 and computerScore < 100:
       # You: 57 Computer: 23
        print(f"You: {humanScore}, Computer: {computerScore}")
        humanScore = human_turn(humanScore)
        # If you reach 100 points or more
        if humanScore >= 100:
            # Print you won,
            print("You won!!!")
            # And end the game
            break

        computerScore = computer_turn(computerScore, computerGoal)
        # If the computer wins 100 points or more
        if computerScore >= 100:
            # Print the computer won
            print("The computer won!!")
            # and end the game
            break

def computer_solo(goal):  # Parameter: computer’s goal for each turn
    # computer_solo(goal) – allows a lonely computer to play by itself with a goal for each turn.
    # Call computer_turn() repeatedly until winning the game.
    # Print the current turns and game score at the end of each turn.
    # Print total turns at the end of the function.
    # Also, return total turns.
    current_turns = 0
    game_score = 0
    # Keep playing until the computers score reaches 100
    while game_score < 100:
        round_total = 0
        # Keep playing until the round reaches the goal
        while round_total < goal:
            # Store the dices to roll_dice func
            dice1, dice2 = roll_dice()
            # Add the round total to the dices
            round_total += dice1 + dice2
            # Pprint the results and total round
            print(f"computer rolled {dice1}, {dice2}. Turn total: {round_total}")
            # If either dice is 1
            if dice1 == 1 or dice2 == 1:
                # Print
                print("computer rolled 1. Turn score lost")
                # Reset the round total to 0
                round_total = 0
                # and end the round
                break
        # Add the gamescore with round total
        game_score += round_total
        # Increment the current turn 1
        current_turns += 1
        # Print the current turn and score
        print(f"turn: {current_turns}, Score: {game_score}")

    return current_turns

# world_championship(games, goal_1, goal_2) – allows two ‘computerplayers’ to play each other a certain number of games.
# For example, play seven games and determine which player wins the most.
# Players have their own goal for each turn.
# Call computer_turn() repeatedly until winning the game.
def world_championship(games, goal_1, goal_2):
    # init games
    player1games = 0
    player2games = 0

    # Design Requirement: Use a for in range loop for the number of games.
    # Use a whileloop to simulate each game.
    # Call computer_turn() for each computer.
    for i in range(games):
        player1score = 0
        player2score = 0

        while True:
            # Store player score to computer_turn function and the goal
            player1score = computer_turn(player1score, goal_1)
            # Check to see if player1's score is greater than or equal score, and if player2's is below their goal
            if player1score >= goal_1 and player2score < goal_2:
                player2score = computer_turn(player2score, goal_2)

            player2score = computer_turn(player2score, goal_2)
            # Check to see if player2's score is greater than or equal score, and if player1's is below their goal
            if player2score >= goal_2 and player1score < goal_1:
                player1score = computer_turn(player1score, goal_1)
            # Check if either of the player reached the goal and different score
            if (player1score >= goal_1 or player2score >= goal_2) and (player1score != player2score):
                break
        # Calculate winner
        if player1score > player2score:
            # Increment
            player1games += 1
        # Otherwise player2 score
        elif player2score > player1score:
            # Increment theirs
            player2games += 1

    return player1games, player2games


if __name__ == "__main__":
    print(roll_dice())
    print(computer_turn(0, 20))
    print("Points", human_turn(57))
    human_vs_computer()
    currentTurns = computer_solo(20)
    print(f"the computer took {currentTurns} turn to win")
    result = world_championship(4, 12, 13)
    print(result)
