import streamlit as st
from names_dataset import NameDataset, NameWrapper
from utils import NAME_EMOJI, display_prediction
import countryflag

@st.cache_resource
def load_name_dataset():
    return NameDataset()

# Initialize NameDataset using the cached function
nd = load_name_dataset()

def predict_sex_and_race_from_name(name):
    result = NameWrapper(nd.search(name)).describe.split(', ')
    sex = result[0] if len(result) > 0 else "Unknown"
    country = result[1] if len(result) > 1 else "Unknown"

    # Get country flag
    if country != "Unknown":
        flag = countryflag.getflag([country])
        country = f"{flag} {country}"

    return sex, country

def process_name_input():
    name = st.text_input(f"{NAME_EMOJI} Enter a name:")
    if name:
        with st.spinner('Predicting...'):
            sex, country = predict_sex_and_race_from_name(name)
            display_prediction(sex, country)
