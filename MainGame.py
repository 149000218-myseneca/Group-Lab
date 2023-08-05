import random

options = ["rock", "paper", "scissors"]
computerOption = random.choice(options)

print("Welcome to Rock, Paper, Scissors!")
playerChoice = input("Enter your choice (rock/paper/scissors): ").lower()

print("Your choice:", playerChoice)
print("Computer's choice:", computerOption)

if playerChoice in options:
    if playerChoice == computerOption:
        print("It's a tie!")
    elif playerChoice == "rock":
        
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

print("Thanks for playing!")
