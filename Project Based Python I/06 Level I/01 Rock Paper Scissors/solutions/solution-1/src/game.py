class Player:
    """Class representing a player in the game."""

    def __init__(self, name: str):
        """
        Initialize a Player.

        :param name: name of the player
        :type name: str
        """
        self.name = name

    def get_choice(self) -> str:
        """
        Prompt the user to enter their choice for the game.

        :return: the user's choice
        :rtype: str
        """
        return input(f"{self.name}, please enter rock, paper, or scissors: ").lower()


class Game:
    """Class representing a Game of Rock, Paper, Scissors."""

    def __init__(self, player1: str, player2: str):
        """
        Initialize a Game.

        :param player1: name of first player
        :type player1: str
        :param player2: name of second player
        :type player2: str
        """
        self.player1 = Player(player1)
        self.player2 = Player(player2)

    def compare(self, p1_choice: str, p2_choice: str) -> str:
        """
        Compare the two player's choices and determine a winner.

        :param p1_choice: choice of player 1
        :type p1_choice: str
        :param p2_choice: choice of player 2
        :type p2_choice: str
        :return: winner announcement
        :rtype: str
        """
        if p1_choice == p2_choice:
            return "It's a tie!"
        elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
             (p1_choice == 'scissors' and p2_choice == 'paper') or \
             (p1_choice == 'paper' and p2_choice == 'rock'):
            return f"{self.player1.name} wins!"
        elif (p2_choice == 'rock' and p1_choice == 'scissors') or \
             (p2_choice == 'scissors' and p1_choice == 'paper') or \
             (p2_choice == 'paper' and p1_choice == 'rock'):
            return f"{self.player2.name} wins!"

    def play(self):
        """
        Run the game.

        Ask players for their choices and display the winner.
        """
        p1_choice = self.player1.get_choice()
        p2_choice = self.player2.get_choice()
        result = self.compare(p1_choice, p2_choice)
        print(result)


if __name__ == "__main__":
    game = Game("Player1", "Player2")
    while True:
        game.play()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
