"""
Rock, Paper, Scissors Game
Author: Priyank Yogesh Panchal, Darshit Parimal Patel & Dev Dineshkumar Patel
Date: 02/Aug/2023
"""

import random

options = ["rock", "paper", "scissors"]

while True:
    computerOption = random.choice(options)

    print("Welcome to Rock, Paper, Scissors!")
    playerChoice = input("Enter your choice (rock/paper/scissors): ").lower()

    print("Your choice:", playerChoice)
    print("Computer's choice:", computerOption)

    if playerChoice in options:
        if playerChoice == computerOption:
            print("It's a tie!")
        elif playerChoice == "rock":
            if computerOption == "scissors":
                print("You win! Rock crushes scissors.")
            else:
                print("Computer wins! Paper covers rock.")
        elif playerChoice == "paper":
            if computerOption == "rock":
                print("You win! Paper covers rock.")
            else:
                print("Computer wins! Scissors cut paper.")
        elif playerChoice == "scissors":
            if computerOption == "paper":
                print("You win! Scissors cut paper.")
            else:
                print("Computer wins! Rock crushes scissors.")
    else:
        print("Invalid choice. Please choose from rock, paper, or scissors.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
