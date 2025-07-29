"""
This program asks the user to input a target value in which the randrange
function generates a random number until one player gets a number closet 
to the target value without going over it. Afterwards, the function prints 
out a phrase indicating which player won.

Author: Gina Lin
Date: February 18, 2024
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45

"""

from random import randrange

def get_yes_or_no(prompt):
    """
    Shows a prompt asking the user to answer a yes or no question.
    Re-prompts the user until a valid choice ("y" or "n") is made
    and then returns the choice.

    prompt: (str) prompt to display to the user

    returns: (str) choice of "y" or "n"
    """
    resp = input(prompt)
    
    while resp != "y" and resp != "n": 
        print("Please enter y/n")
        resp = input(prompt)
    # This implementation simply returns whatever the user enters.
    # Modify it so that it keeps prompting until they enter "y" or "n".
    return resp

def get_value_between(msg, low, hi):
    """
    Shows a message and then prompts the user to enter a number between
    low and hi (inclusive) and returns the user's choice.
    Re-prompts the user until a valid choice is made.

    msg: (str) message to display to the user
    low: (int) the smallest allowable value
    hi: (int) the largest allowable value

    returns: (int) the user's selected value
    """    
    print("What is the target value? ")
    target_value = input("Enter a number between 7 and 21: " )
    
    while int(target_value) <7 or int(target_value) >21:
        target_value = input("Enter a number between 7 and 21: " )
    return target_value

def roll(score, opp, target):
    """
    Shows the current scores and target, then asks the user if they want
    to roll the die. If so, simulates rolling the die and displays the
    result. Then returns the rolled value, or 0 if the player did not roll.

    score: (int) the player's current score
    opp: (int) the opponent's current score
    target: (int) the target value

    returns: (int) the rolled value, or 0 if the player did not roll
    """
    print("Your score is %d; your opponent's score is %d; the target is %d" % 
    (score, opp, target))
    question = "Would you like to roll (y/n)? "
    rollinput = 0
    choice = get_yes_or_no(question)
    if choice == "y":
        rollinput = randrange(7)
        print("You rolled: " + str(rollinput))
    return rollinput
    
def play_game(target):
    """
    Play the game until someone wins

    target: (int) the target value

    returns: none
    """
    player1 = 0
    player2 = 0 
    
    while True:
        player1roll = roll(player1, player2, target)
        player1 = player1roll + player1
        print("Your score is %d" % (player1))
        if player1 > target:
            print("Player 2 won!")
            return
        elif player1 == target and player2 == target:
            print("It's a draw! ")
            return
        else:
            player2roll = roll(player1, player2, target)
            player2 = player2roll + player2
            print("Your score is %d" % (player2))
            if player2 > target:
                print("Player 1 won!")
                return 
def main():
    print("Welcome to the dice game!")
    # this is the code for testing the get_yes_or_no function 
    num = get_value_between("What is the target value?", 7, 21)
    play_game(int(num))

# makes sure main is only called when you run this program directly
if __name__=='__main__':
    main()
