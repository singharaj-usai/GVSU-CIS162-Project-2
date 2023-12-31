﻿# GVSU-CIS162-Project-2

<h2 align="center">
CIS 162 Project 2
A Dice Game Called Pig
</h2>

### Due Date
• Wednesday October 18 3:00 pm (EXTENDED TO FRIDAY OCT 20 5 PM)

### Before Starting the Project
• Read Ch 5 and Ch 7

• Read this entire project description before starting

### Learning Objectives
After completing this project you should be able to:

• write methods to meet specific requirements

• *write* conditional statements with boolean expressions

• *write* a looping construct

• *develop* a collection of methods

### Game Rules
• The game requires two six-sided dice.

• Players take turns until someone wins by earning at least 100 points. A player could play alone as well but probably not as fun! More than two peole can play but not for this project.

• Players begin a turn by rolling both dice and adding the points. A player continuesrolling and accumulating points until rolling a '1' or choosing to 'hold'. If theplayer rolls a 1 then all points from this turn are lost. If the player rolls a pair of1s then all player points are lost (set to zero). By holding before rolling a 1, theplayer stores the points and passes dice to the other player.

• Player rolls 4 and 5 – add 9 to this turn

• Player rolls 4 and 1 – player loses turn and points for this turn

• Player rolls 1 and 1 – player loses turn and ALL points. Score goes to zero.

• Play moves to the next player

### Step 1: Create a New pyCharm Project

### Step 2: Create a file called PigGame
Create a file, called *PigGame.py*. Do not create additional methods or make any changes to thefollowing requirements without approval from your instructor.

#### Methods
• `roll_dice()` - Call `random.randint(1,6)` twice to simulate rolling two dice.

Refer to zyBook 2.9 for more information about the `random` module. Return both as separate values. This method is called by several other methods. 

**Parameters**: none

**Returns**: two random values between 1 - 6

**Your Testing**: Testing code with randomness is challenging. Your best approach is tocall `roll_dice()` many times and pay attention to the returned values.

`if __name__ == '__main__':
    print(roll_dice())`

**Out Testing**: copy your partial solution to zyBook 18.7 for initial testing. Select“Submit Mode” and then “Submit for grading” (1 of 9 tests should pass).

• `computer_turn(game_score, goal)` - performs the computer’s turn. Computer is provided a `goal` to achieve and then stop rolling for the current turn. Turn total starts at zero. Call `roll_dice( )` to roll both dice. Keep rolling until a 1 is rolled or the goal is achieved. There are three possible outcomes. 1) If double 1s are rolled, set `game_score` to zero and end the turn. 2) If a single 1 is rolled, set the current turn score to zero and end the turn. There is no change to game_score. 3) Otherwise, add both dice to the turn score. Print the rolled dice and turn score after each roll. At the end of the turn, return the updated `game_score`.

Computer rolled 5,6 Turn total: 43
Computer rolled 3,1 Turn total: 0

**Design Requirement**: Use a while loop

**Parameters**: current game score and the minimal goal for this turn

**Returns**: updated game score

**Your Testing**: Testing code with randomness is challenging. Your best approach is to call `computer_turn()` many times with different arguments and pay attention to the output.

`if __name__ == '__main__':
    computer_turn(0, 20))`

**Out Testing**: copy your partial solution to zyBook 18.7 for additional testing. (4 of 9tests should pass)

• `human_turn(game_score)` – supports a person taking one turn. Player continues to roll both dice until one of three options: 1) rolls a 1 and loses turn, 2) chooses to end turn by not rolling, or 3) wins game by earning at least 100 points. If the player chooses to stop, add the current turn total to `game_score`. Use a `while loop` to repeatedly roll the dice and ask the player at the end of the loop whether she wants to roll again. Sample output:

You rolled 5,4 Turn total: 9

Roll again (y/n)? y

You rolled 3,3 Turn total: 15
Roll again (y/n)? y

You rolled 3,2 Turn total: 20

Roll again (y/n)? n

**Design Requirement**: Use a while loop

**Parameters**: current game score

**Returns**: updated game score

**Your Testing**: Testing code with randomness is challenging. Your best approach is to call `human_turn()` many times with different arguments and pay attention to the output.

`if __name__ == '__main__':
human_turn(57))`

**Out Testing**: there is no automated testing for this method. Your instructor will test during your demonstration.

• `human_vs_computer()` – supports a full game of person versus the computer. Play continues until someone wins with at least 100 points. Human goes first. Computer’s goal is 20 each turn. Call `human_turn()` and `computer_turn()` within a while loop foreach turn. Print the current score for each player (see sample output). Note, the whileloop will be short within only about five lines of code. One of which will be similar to:

`human_score = human_turn(human_score)`

Print an appropriate message at the end of the game depending on who wins. Sample output from the end of a game:

You: 57 Computer: 23

You rolled 2,2 Turn total: 4

Roll again (y/n)? y

You rolled 6,5 Turn total: 15

Roll again (y/n)? y

You rolled 5,6 Turn total: 26

Roll again (y/n)? y

You rolled 2,3 Turn total: 31

Roll again (y/n)? n

Computer rolled 5,1 Turn total: 0

You: 88 Computer: 23

You rolled 6,6 Turn total: 12

You: 100 Computer: 23

Congratulations!

**Design Requirement**: Use a while loop

**Parameters**: none

**Returns**: none

**Your Testing**: Testing code with randomness is challenging. Your best approach is to call `human_vs_computer()` many times with different arguments and pay attention to the output.

**Out Testing**: there is no automated testing for this method. Your instructor will test during your demonstration

• `computer_solo(goal)` – allows a lonely computer to play by itself with a goal for each turn. Call `computer_turn()` repeatedly until winning the game. Print the current turns and game score at the end of each turn. Print total turns at the end of the function. Also, return total turns.

Sample output from the end of a game:

Turn: 15 Score: 72

Computer rolled 6,4 Turn total: 10

Computer rolled 6,4 Turn total: 20

Turn: 16 Score: 92

Computer rolled 2,2 Turn total: 4

Computer rolled 5,6 Turn total: 15

Computer rolled 2,6 Turn total: 23

Turn: 17 Score: 115

Turns: 17

**Design Requirement**: Use a while loop

**Parameter**: computer’s goal for each turn

**Returns**: total turns played until winning

**Your Testing**: Testing code with randomness is challenging. Your best approach is to call `computer_solo()` many times with different arguments and pay attention to the output.

• `world_championship(games, goal_1, goal_2)` – allows two ‘computerplayers’ to play each other a certain number of games. For example, play seven games and determine which player wins the most. Players have their own goal for each turn. Call `computer_turn()` repeatedly until winning the game.

Players get the same number of turns. For example, second player gets a turn even if the first player gets 100 points. In this scenario, the player with the most points wins the game. After all games are complete, print results for player 1 and player 2.

Sample output after nine games:

Computer rolled 6,6 Turn total: 34

Computer rolled 1,2 Turn total: 0

Alexa: 127 Siri: 82

Alexa: 5 wins Siri: 4 wins

**Design Requirement: Use a for in range loop for the number of games**. Use a whileloop to simulate each game. Call `computer_turn()` for each computer.

**Parameter**: number of games, goal for first computer, goal for second computer

**Returns**: games won by computer one and computer two (two values)

**Out Testing**: copy your partial solution to zyBook 18.7 for testing (all tests should pass).

### Reducing User Errors

Good practice includes reducing possible data entry errors. This may require confirming a number is between 1 – 100 as requested, confirming menu choices are valid, or confirming yes/no responses.

ACTION: After writing the following function, update `human_turn()` to call `validate_response()` rather than prompt and read the input within `human_turn()`.

• `validate_response(prompt, response_1, response_2)` – supports repetitive request for a response until one of two valid responses. For example, keep printing the prompt until the user responds with t or f. The beauty of this function is it can be used in a variety of other programs and situations. Sample output:

Turn left or right (left/right)? neither

Turn left or right (left/right)? west

Turn left or right (left/right)? l

Turn left or right (left/right)? right

function finally returns “right”

**Design Requirement**: Use a while loop

**Parameters**: prompt, valid response, second valid response

**Returns**: valid response

**Your Testing**: Testing code with randomness is challenging. Your best approach is to call () many times with different arguments and pay attention to the output.

`if __name__ == '__main__':
validate_response(57))`

**Out Testing**: there is no automated testing for this method. Your instructor will test during your demonstration.

### Support Instructor Testing
Include the following code at the bottom of your solution. This will help your instructor quickly test these methods.

`if __name__ == '__main__':
pass#human_vs_computer()
#human_turn(10)
#validate_response("Does this work (t/f)?",'t','f')`

### Coding Style (10 pts)

Good programming practice includes writing elegant source code for the human reader. Follow the [Style Guide for Python Code](https://peps.python.org/pep-0008/). For CIS 162, follow these additional guidelines:

• Comments are at the same indentation as the corresponding code

• Provide comments before most if statements

• Provide comments before most loops

• Blank lines before every comment

• Use docstrings to describe classes and functions (see 9.10) (later in term)

• Class attribute names should begin with an underscore (later in term)

### Turn In
Submit the cover page and journal to Blackboard as a PDF.

• Cover page - Provide a cover page that includes your name, a title, and an appropriate picture
or clip art for the project.

• Signed Pledge – The cover page must include the following signed pledge: "I pledge that this
work is entirely mine, and mine alone (except for any code provided by my instructor). "
In addition, provide names of any people you helped or received help from. Under no
circumstances do you exchange code electronically. You are responsible for
understanding and adhering to the [School of CIS Guidelines for Academic Honesty](http://www.cis.gvsu.edu/academic-honesty/).

• Programming Journal (2nd page) – Professional coders track their time in fifteen-minute
increments and journal their activities. What challenges did they encounter and how did
they solve the issue? What portion of the program was completed and when? Include
dates and times. In addition, provide names of any people you helped or received help
from.

• Source code – your source code will be reviewed within zyBook.

### Grading Criteria
• Pass all zyBook tests (70 pts)

• Pass instructor tests during demonstration and solution meets all design requirements (15
pts)

• Signed pledge and programming journal (5 pts)

• Attractive source code with appropriate comments to describe separate sections of the
solution. All files should have the following header at the top. (10 pts)

```pycon
'''
YOUR NAME
Brief description of the code for other programmers to read
I certify that this code is mine, and mine alone, in accordance with
GVSU academic honesty policy.
COMPLETION DATE
'''
```

• Late Policy. Projects are due at the START of the class period. However, you are
encouraged to complete a project even if you must turn it in late. Each 24-hour period
submitted late (-10 pts). Weekends and holidays are free days. Projects are not accepted
more than five days late without prior instructor approval

