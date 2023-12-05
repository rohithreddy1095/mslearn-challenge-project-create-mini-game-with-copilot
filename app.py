#import random module
import random

#create a list of three possible choices 'rock', 'paper', or 'scissors'
choices = ['rock', 'paper', 'scissors']



#Initialize variables to keep track of the number of rounds and the number of wins for the user and the computer
rounds = 0
user_wins = 0
computer_wins = 0
ties = 0

#Print a message to the user letting them know that the game is starting and how many rounds they will be playing
print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Welcome to my Rock-Paper-Scissors game...")
print("-------------------")

#Ask the user for their choice of 'rock', 'paper', or 'scissors' (assigning that value to a variable)
#Validate user selection
#Stop the game if the user types in 'quit' or 'q'
#If the user makes a valid selection, then get a random selection for the computer (assigning that value to a variable)
#Print the user's selection
#Print the computer's selection
#Determine who won and display the result to the user:
#Rock beats Scissors
#Paper beats Rock
#Scissors beats Paper
#Tie if the selections are the same
#Keep track of the number of wins for the user and the computer
#Ask the user if they want to play again (assigning that value to a variable)
#Validate user selection
#Stop the game if the user types in 'quit' or 'q'
#If the user makes a valid selection, then repeat from step 1 (above)
#When the game is over, print out the total number of wins for the user and for the computer
#Print out a message thanking the user for playing
#Print out a message with the final results
#Print a message to let the user know the game is ending

while True:
    user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
    if user_choice in choices:
        print("You chose: ", user_choice)
    elif user_choice == "quit" or user_choice == "q":
        print("You chose to quit. Goodbye!")
        break
    else:
        print("Invalid selection. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print("The computer chose: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Rock beats scissors. You win!")
        user_wins += 1
    elif user_choice == "rock" and computer_choice == "paper":
        print("Paper beats rock. You lose!")
        computer_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("Paper beats rock. You win!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Scissors beats paper. You lose!")
        computer_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Scissors beats paper. You win!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Rock beats scissors. You lose!")
        computer_wins += 1

    rounds += 1
    print("-------------------")
    print("Round: ", rounds)
    print("Wins: ", user_wins)
    print("Losses: ", computer_wins)
    print("Ties: ", ties)
    print("-------------------")

    play_again = input("Would you like to play again? (yes/no) ")
    if play_again == "yes":
        continue
    elif play_again == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid selection. Please try again.")
        continue

print("-------------------")
print("Final Results:")
print("-------------------")
print("Total Rounds: ", rounds)
print("Total Wins: ", user_wins)
print("Total Losses: ", computer_wins)
print("Total Ties: ", ties)
print("-------------------")
print("Thanks again for playing!")
print("-------------------")
