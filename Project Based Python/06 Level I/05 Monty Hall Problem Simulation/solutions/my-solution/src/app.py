import streamlit as st
from src.monty_hall import simulate_game
import time

st.title(":zap: Monty Hall Simulation")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Monty_open_door.svg/640px-Monty_open_door.svg.png", width=400)
num_games = st.number_input(
    "Enter number of games to simulate",
    min_value=1, max_value=100000,
    value=100
)

col1, col2 = st.columns(2)
col1.subheader('Win Percentage without Switching')
col2.subheader('Win Percentage with Switching')

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_no_switch = 0
wins_switch = 0

for i in range(num_games):
    num_wins_with_switching, num_wins_without_switching = simulate_game(1)
    wins_no_switch += num_wins_without_switching
    wins_switch += num_wins_with_switching

    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])

    time.sleep(0.01)
