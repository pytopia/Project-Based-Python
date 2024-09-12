import streamlit as st

# Emojis
TITLE_EMOJI = "🧠"
NAME_EMOJI = "🧑‍🦰"
IMAGE_EMOJI = "🖼️"
SEX_EMOJI = "🧬"
RACE_EMOJI = "🌍"

def display_prediction(sex, race):
    st.write(f"{SEX_EMOJI} Sex: **{sex}**")
    st.write(f"{RACE_EMOJI} Race/Ethnicity: **{race.title()}**")
