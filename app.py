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
            game_score += turnTotal
            return game_score

        turnTotal += dice1 + dice2

def human_turn(game_score):
    totalScore = 0
    while True:
        dice1, dice2 = roll_dice()
        print(f"you rolled {dice1}, {dice2} turn total: {totalScore}")

        if dice1 == 1 or dice2 == 1:
            print("you rolled 1. Turn lost")
            return game_score

        choice = input("Roll again? (y/n) ").strip().lower()

        if choice != "y":
            game_score += totalScore
            return game_score


        totalScore += dice1 + dice2
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
        if humanScore >= 100:
            print("You won!!!")
            break

        computerScore = computer_turn(computerScore, computerGoal)
        if computerScore >= 100:
            print("The computer won!!")
            break

def computer_solo(goal):  # Parameter: computer’s goal for each turn
    # computer_solo(goal) – allows a lonely computer to play by itself with a goal for each turn.
    # Call computer_turn() repeatedly until winning the game.
    # Print the current turns and game score at the end of each turn.
    # Print total turns at the end of the function.
    # Also, return total turns.
    current_turns = 0
    game_score = 0

    while game_score < 100:
        round_total = 0
        while round_total < goal:
            dice1, dice2 = roll_dice()
            round_total += dice1 + dice2
            print(f"computer rolled {dice1}, {dice2}. Turn total: {round_total}")

            if dice1 == 1 or dice2 == 1:
                print("computer rolled 1. Turn score lost")
                round_total = 0
                break

        game_score += round_total
        current_turns += 1
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

        while player2score < 100 and player1score < 100:
            player1score = computer_turn(player1score, goal_1)
            player2score = computer_turn(player2score, goal_2)

        if player1score >= 100:
            player1games += 1
        else:
            player2games += 1

    return player1games, player2games


if __name__ == "__main__":
    print(roll_dice())
    print(computer_turn(0, 20))
    print("Points", human_turn(57))
    human_vs_computer()
    currentTurns = computer_solo(20)
    print(f"the computer took {currentTurns} turn to win")
    world_championship()
