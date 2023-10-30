import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_user_choice(self):
        user_choice = input("Enter your choice (rock/paper/scissors): ")
        if user_choice.lower() in self.choices:
            return user_choice
        else:
            print("Invalid choice. Please make sure your choice is in 'rock', 'paper' or 'scissors'.")
            return self.get_user_choice()

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "Congratulations, you won!"
        else:
            return "Oh no, the computer won!"

    def play(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print('Computer chose: ', computer_choice)
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissors()

    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break
