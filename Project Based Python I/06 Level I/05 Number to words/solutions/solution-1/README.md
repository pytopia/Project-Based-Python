# README.md

## Project Name: Python Number to Words Converter

## Description:

The Python Number to Words Converter project contains a Python program that converts numerical input from a user into corresponding words. The minimal interface requests an input of a number from the user, which it then processes and returns in word format.

For example, if the user enters "12345", the program will output "Twelve thousand three hundred and forty five". The program is equipped to handle numbers between 0 and 999,999,999,999.

## Getting Started:

This project includes the following main Python file:

- `main.py`: The main script handles user input and calls the num_to_word function in the same script.

Other required modules and necessary constants are in a separate Python file:

- `constants.py`: This file contains all the constant lists and dictionaries that are necessary for the number-to-word conversion. These constants include UNDER_20, TENS and ABOVE_100.

To run the program, follow these steps:

1. Navigate to the project folder in your terminal.
2. Run the main.py script using the command `python main.py`.
3. When requested, enter a number to be converted into words.

## Functions and Definitions:

- `num_to_word`: This function accepts an integer and converts it into equivalent English words. It checks the number length and based on the length, the number is converted into words.

- `main`: This function prompts the user to enter an integer number and checks if it's within the specified range (0 to 999999999999). If so, it calls the function num_to_word to convert the input number to words.

- Constants:
  - UNDER_20: This list stores values for numbers under 20.
  - TENS: This list stores values for every tenth number up until 100.
  - ABOVE_100: This dictionary stores values for numbers above 100 and places like 1_000, 1_000_000 and 1_000_000_000.
