import random
from typing import List


class RockPaperScissors:
    """
    Main class for the game Rock, Paper, Scissors
    """
    def __init__(self):
        self.choices: List[str] = ['rock', 'paper', 'scissors']

    def get_user_choice(self) -> str:
        """Method to get the user's choice.

        :return: User's choice as a string
        """
        user_choice: str = input("Enter your choice (rock/paper/scissors): ")
        if user_choice in self.choices:
            return user_choice
        else:
            print("Invalid choice. Please make sure your choice is in 'rock', 'paper' or 'scissors'.")
            return self.get_user_choice()

    def get_computer_choice(self) -> str:
        """Method to select the computer's choice.

        :return: Computer's choice as a string
        """
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Method to decide game winner based on the rules.

        :param user_choice: The user's choice
        :param computer_choice: The computer's choice
        :return: Game outcome as a string
        """
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "Congratulations, you won!"
        else:
            return "Oh no, the computer won!"

    def play(self):
        """Main method to play Rock, Paper, Scissors"""
        user_choice: str = self.get_user_choice()
        computer_choice: str = self.get_computer_choice()
        print('Computer chose: ', computer_choice)
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissors()

    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break
