import streamlit as st
import pandas as pd
import time

from monty_hall import simulate_games

# Title of the application
st.image('src/images/banner.png')

num_games = st.number_input("Enter number of games to simulate", min_value=1, value=100)

# Create two lists to hold win percentages for both cases
wins_no_switch = 0
wins_switch = 0

col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
chart1 = col1.empty()
no_switch_history = []

col2.subheader("Win Percentage With Switching")
chart2 = col2.empty()
switch_history = []


for i in range(num_games):
    # Simulate one game at a time
    num_wins_without_switching, num_wins_with_switching = simulate_games(1)

    # Calculate win percentages for both cases and add to lists
    wins_no_switch += num_wins_without_switching
    wins_switch += num_wins_with_switching

    no_switch_history.append(wins_no_switch / (i+1))
    switch_history.append(wins_switch / (i+1))
    
    data1 = pd.DataFrame({
        "Trial": range(1, len(no_switch_history) + 1),
        "Switch": no_switch_history
    })

    data2 = pd.DataFrame({
        "Trial": range(1, len(switch_history) + 1),
        "Switch": switch_history
    })

    data1 = data1.set_index("Trial")
    chart1.line_chart(data1)
    data2 = data2.set_index("Trial")
    chart2.line_chart(data2)

    # Add a delay to create a slow loop effect
    time.sleep(0.01)
