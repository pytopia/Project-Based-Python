import random


def get_user_choice():
    """Gets the user's choice."""
    print("\n1. Rock\n2. Paper\n3. Scissors")
    user_choice = int(input("Enter your choice: "))
    while user_choice < 1 or user_choice > 3:
        user_choice = int(input("Enter a valid choice: "))
    items = {1: 'rock', 2: 'paper', 3: 'scissors'}
    return items[user_choice]


def get_computer_choice():
    """Gets the computer's choice."""
    computer_choice = random.randint(1, 3)
    items = {1: 'rock', 2: 'paper', 3: 'scissors'}
    return items[computer_choice]


def determine_winner(user_choice: str, computer_choice: str):
    """Determines the winner."""
    winners = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if user_choice == computer_choice:
        return "It's a tie"
    elif winners[user_choice] == computer_choice:
        return "User wins"
    else:
        return "Computer wins"


def play():
    """Plays the game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("User chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))


if __name__ == "__main__":
    play()
