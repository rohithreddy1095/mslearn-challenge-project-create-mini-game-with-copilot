# Import the required module

# Define the choices

# Function to get the computer's choice

# Function to get the user's choice

# Function to determine the winner

# Function to play the game

# Initialize variables for score and rounds

# Loop to play multiple rounds

# Increment variables based on round result

# Prompt to ask user to play again

# Handle invalid input for play again prompt

# Break loop if user doesn't want to play again

# Print final score

# Call function to start the game

# Test the game

# Run the game

# Path: app_new.py

# Import the required module
import random

# Define the choices
choices = ['rock', 'paper', 'scissors']

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(choices)

# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
        if user_choice in choices:
            print("You chose: ", user_choice)
            return user_choice
        elif user_choice == "quit" or user_choice == "q":
            print("You chose to quit. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
            continue

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    # Print out a message with the final results
    # Print a message to let the user know the game is ending
    if user_choice == computer_choice:
        print("It's a tie!")
        return None
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Rock beats scissors. You win!")
        return True
    elif user_choice == "rock" and computer_choice == "paper":
        print("Paper beats rock. You lose!")
        return False
    elif user_choice == "paper" and computer_choice == "rock":
        print("Paper beats rock. You win!")
        return True
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Scissors beats paper. You lose!")
        return False
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Scissors beats paper. You win!")
        return True
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Rock beats scissors. You lose!")
        return False
    
# Function to play the game
def play_game():
    # Initialize variables for score and rounds
    rounds = 0
    user_wins = 0
    computer_wins = 0
    ties = 0

    # Loop to play multiple rounds
    while True:
        # Prompt to ask user to play again
        user_choice = get_user_choice()
        if user_choice == "quit" or user_choice == "q":
            break

        # Get the computer's choice
        computer_choice = get_computer_choice()
        print("The computer chose: ", computer_choice)

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        if result == None:
            ties += 1
        elif result == True:
            user_wins += 1
        elif result == False:
            computer_wins += 1

        # Increment variables based on round result
        rounds += 1
        print("-------------------")
        print("Round: ", rounds)
        print("Wins: ", user_wins)
        print("Losses: ", computer_wins)
        print("Ties: ", ties)
        print("-------------------")

        # Handle invalid input for play again prompt
        while True:
            play_again = input("Would you like to play again? (yes/no) ")
            if play_again == "yes":
                break
            elif play_again == "no":
                print("Thanks for playing!")
                break
            else:
                print("Invalid selection. Please try again.")
                continue
        if play_again == "no":
            break

    # Print final score
    print("-------------------")
    print("Final Results:")
    print("-------------------")
    print("Rounds Played: ", rounds)
    print("Wins: ", user_wins)
    print("Losses: ", computer_wins)
    print("Ties: ", ties)
    print("-------------------")

# Call function to start the game
play_game()

