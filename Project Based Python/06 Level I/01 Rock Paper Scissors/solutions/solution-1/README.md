# Rock Paper Scissors Game

This project aimed to construct a simple and interactive Rock, Paper, Scissors game using Python. It resulted in a command-line game where two players can compete against each other. To further immerse the users, an option was provided to replay the game without restarting the program.

## Description

The Rock, Paper, Scissors game was structured using Object Oriented Programming (OOP), providing a clear overview of the game logic and making the code reusable and easier to maintain and debug.

The solution is divided into two classes:

- Player Class: Defines a player object with name and implements a method to take the choice (rock, paper or scissors) input from the player.

- Game Class: Defines the game rules and logic. It takes two Player objects as input and has a method to initiate game play. The compare method compares the choices of the players and decides the result of a round. The play method initiates a round and prints the result.

A safeguard was implemented to check whether the script was executed as a main program before initiating the game. This allows the module to be imported and tested separately without automatically running the game.

The game is run in a loop until the player decides to stop, enabling replay without restarting the program.

# How to Run

To run the Rock, Paper, Scissors game, make sure you have Python installed on your system. After ensuring Python is installed, follow these steps:

- Open a terminal window and navigate to the project folder.
- Add the project folder to your PYTHONPATH environment variable by running the following command in the terminal:

```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
```

- Run the game by executing the following command in the terminal:

```bash
python src/game.py
```

# Requirements

- Python 3.7 or higher: The game is developed in Python and needs a Python interpreter to run.

## Future Enhancements

- More interactive user interface.
- Track scores across multiple games.
- Game history and statistics.
- Multiple game types (best of 3, 5 etc).
- Option for computer opponent with random or predefined patterns.
