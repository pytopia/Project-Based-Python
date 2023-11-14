# Tic-Tac-Toe

This project implements the classic two-player game Tic-Tac-Toe using Python. The game board is made of nine cells numbered from 1 to 9, which players mark alternately with an 'O' or an 'X'. The goal is to be the first to mark three 'O's or 'X's diagonally, horizontally, or vertically. The code base utilizes Python's object-oriented programming, defining a TicTacToe class with attributes and methods to represent the game's features. The Python random module is employed to randomly select the first player.

## Project Structure
The core of this project is a single Python file, tictactoe.py. It contains the TicTacToe class with its associated attributes and methods.

Here is a brief overview of the class methods:

* `__init__()` initializes the game board and randomly selects the first player.
* `get_random_first_player()` chooses whether 'X' or 'O' will play first.
* `fix_spot()` allows a player to mark a cell on the board.
* `has_player_won()` checks if a player has won the game.
* `is_board_filled()` checks if the game board is completely filled.
* `swap_player_turn()` toggles the active player.
* `show_board()` prints out the current state of the game board.
* `start()` begins the game loop, processing user input and game updates.

## Requirements
To run this project, you will need:

* Python 3.x

The project also assumes that you have a basic understanding of Python programming and object-oriented programming concepts.

## Usage
Running the tictactoe.py script in a Python environment will start the game. Players will be asked to input a number from 1 to 9 to mark a cell on the board, with '1' being the first cell and '9' being the last cell. Invalid inputs or attempts to mark already filled cells will prompt the game to request for input again.

Users will see the game board after every turn and be notified on the console screen if a player wins or if the game ends in a draw.

## Learning Outcomes
Completing this project will help reinforce your understanding of Python's object-oriented programming concepts, improve your problem-solving skills, and show you how to model the states and behavior of a system in code. Furthermore, you will gain practical experience in implementing a simple game logic.

## Future Enhancements
The game currently supports a text-based interface. Future enhancements could include a graphical user interface (GUI), adding a computer opponent for single-player games, and improving the user interface for a visually appealing and user-friendly experience.
