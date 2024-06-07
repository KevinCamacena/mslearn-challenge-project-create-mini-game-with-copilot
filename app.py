# Rules:
# Rock beats sicssors
# Scissors beats paper
# Paper beats rock

import random



def game_logic(wins, loses, ties):
    # Generate a random number between 0 and 2
    # 0 -> rock
    # 1 -> paper
    # 2 -> scissors

    game_options = ["rock", "paper", "scissors"]
    computer_choice = random.randint(0, 2)

    valid_input = False

    while not valid_input:
        # Read from the terminal the player's choice
        player_choice = input("Enter your choice: ")
        valid_input = validate_choice(player_choice)
        if not valid_input:
            print("Invalid choice. Please enter rock, paper, or scissors")

    # Convert the player's choice to a number
    if player_choice == "rock":
        player_choice = 0
    elif player_choice == "paper":
        player_choice = 1
    else:
        player_choice = 2

    print(f"Player choice: {game_options[player_choice]}")
    print(f"Computer choice: {game_options[computer_choice]}")

    # Check who won
    if player_choice == computer_choice:
        print("It's a tie")
        ties += 1
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
        wins += 1
    elif player_choice == 1 and computer_choice == 0:
        print("You win!")
        wins += 1
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")
        wins += 1
    else:
        print("Computer wins!")
        loses += 1

    return wins, loses, ties


# Validate the player's choice
def validate_choice(choice):
    # Convert choice to lowercase
    choice = choice.lower()
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return True
    else:
        return False
    
def main():
    wins = 0
    loses = 0
    ties = 0
    keep_playing = True
    while keep_playing:
        print("Welcome to Rock, Paper, Scissors Game!")
        print("Enter your choice: rock, paper, or scissors")
        # Should improve this
        wins, loses, ties = game_logic(wins, loses, ties)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            keep_playing = False
            print("Wins: ", wins)
            print("Loses: ", loses)
            print("Ties: ", ties)
            print("Thanks for playing!")


if __name__ == "__main__":
    main()
