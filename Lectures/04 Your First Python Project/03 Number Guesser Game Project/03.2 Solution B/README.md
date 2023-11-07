# Number Guesser Game - Solution B

## Overview

This solution provides a modular approach to the Number Guesser Game. The game generates a random number between 1 and 100, and the user is prompted to guess this number. For each incorrect guess, the user receives a hint and their score is reduced.

## Directory Structure

```
number_guesser/
|-- src/
| |-- main.py
| |-- game_logic/
| | |-- init.py
| | |-- number_generator.py
| | |-- hint_generator.py
| | |-- scorer.py
| |-- utils/
| | |-- init.py
| | |-- input_validator.py
|-- README.md
|-- requirements.txt
```

## How to Run

1. Navigate to the main project directory (`number_guesser`).
2. Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```

Follow the on-screen prompts to play the game.

## Modules

- `src/main.py`: The main entry point of the game. It handles the game loop, user input, and display.
- `src/game_logic/`: Contains the core game logic.
  - `number_generator.py`: Generates a random number.
  - `hint_generator.py`: Provides hints based on the user's guess.
  - `scorer.py`: Manages the scoring system.
- `src/utils/`: Contains utility functions.
  - `input_validator.py`: Validates user input.
