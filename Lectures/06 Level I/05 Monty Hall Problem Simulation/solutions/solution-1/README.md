# Monty Hall Simulation Interactive Dashboard

## Description

This implementation solves the famous Monty Hall problem, presenting an interactive dashboard where you can simulate numerous iterations of the game and visibly note the win percentages in both scenarios, i.e., switching and not switching the chosen door.

## Project Structure

```
.
├─ README.md
├─ requirements.txt
└─ src
   ├─ monty_hall.py
   └─ app.py
```
- `README.md`: This descriptive file
- `requirements.txt`: Contains all the required modules and libraries needed to run the project
- `src/monty_hall.py`: Contains the Python program to simulate the Monty Hall game
- `src/app.py`: The Streamlit application file to display an interactive dashboard

## Requirements

- Python 3.7 or higher
- Streamlit

To install necessary packages, run `pip install -r requirements.txt`.

## Usage

You can play the Monty Hall game simulation by adding the `src` directory to the PYTHONPATH and running:

`python3 src/monty_hall.py`

To start the Streamlit dashboard, run: 

`streamlit run src/app.py`

## Results

On running the Streamlit application, you will see an input field where you can specify the number of games to simulate. The app will then perform a simulation for each game, both where the contestant switches doors and where they don't. Lastly, the dashboard will display the win percentages dynamically as two separate line charts - showing how the likelihood of winning changes based on your decision to switch or not to switch doors.
