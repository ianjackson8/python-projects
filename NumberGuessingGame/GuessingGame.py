'''
=== Number Guessing Game ===
- User is asked for a difficulty (easy, medium, hard)
- Generates a random number
- User has a limited number of guesses
'''

import os
import random

# global variables
mode = ""
maxNum = 0
maxGuesses = 0

# main function
def main():
    """
    main function of the script
    """
    global mode
    term = False

    # while game is still running
    while term != True:
        # run menu, sets difficulty
        mode = menu()
        
        # check if exit
        if mode == "exit":
            term = True
            return

        # set game parameters based on mode
        setParameters(mode)

        clearTerminal()

        playGame()

def menu():
    '''
    lets the user decide what difficulty to play on
    returns character representing mode or if to end game play
    '''
    validInput = False

    print("What difficulty would you like to play on?")

    while validInput != True: 
         # get user input
        userIn = input("a.) Easy\nb.) Medium\nc.) Hard\nd.) Exit\n")

        # validate input
        if userIn.isalpha() and userIn in ["a", "b", "c", "d"] :
            validInput = True
        else: 
            print("Invalid input, try again")

    # return mode
    if userIn == "a":
        return "easy"
    elif userIn == "b":
        return "med"
    elif userIn == "c":
        return "hard"
    elif userIn == "d":
        return "exit"

def setParameters(gameMode):
    '''
    Sets the game parameters based on the mode
    Easy - 1-10 with 10 guesses
    Medium - 1-50 with 5 guesses
    Hard - 1-100 with 3 guesses
    '''
    global maxNum, maxGuesses

    if gameMode == "easy":
        maxNum = 10
        maxGuesses = 10
    elif gameMode == "med":
        maxNum = 50
        maxGuesses = 5
    elif gameMode == "hard":
        maxNum = 100
        maxGuesses = 3

def clearTerminal():
    '''
    Clears the terminal screen based on the operating system
    '''
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For UNIX/Linux/Mac
        os.system('clear')

def playGame() :
    '''
    function to play the game
    '''
    global maxNum, maxGuesses

    # generate number
    target = random.randint(1, maxNum)
    numGuesses = 0
    isWin = False

    print(f"Guess a number between 1 and {maxNum}")
    print(f"You have {maxGuesses} guesses")

    while isWin == False:
        if numGuesses >= maxGuesses:
            print("You lost, try again")
            print(f"The number was {target}\n")
            return

        userIn = input(f"Guess {numGuesses+1}: ")

        try:
            # convert string to int
            guess = int(userIn)
        except ValueError:
            print("Please input a digit")

        # check conditions
        if guess < 0 or guess > maxNum:
            print("Please input within range")
        elif guess > target:
            print("The target number is less than your guess")
        elif guess < target:
            print("The target number is greater than your guess")
        elif guess == target:
            print(f"Correct! You won in {numGuesses+1} number of guesses")
            print("\n")
            isWin = True
        
        numGuesses = numGuesses + 1

# check if script is being run directly
if __name__ == "__main__":
    # call main function
    main()
