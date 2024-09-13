import streamlit as st
from src.web_scraper import search_google
from src.text_processor import prepare_context
from src.llm_interface import call_llm
from src.constants import openai_models
from dotenv import load_dotenv
load_dotenv()

st.image("src/images/banner.png")
st.title("Fake News Detector")
st.sidebar.header("About")
st.sidebar.info("This app uses web scraping and AI to analyze whether a given news headline or claim might be fake news.")
model = st.sidebar.selectbox("Select a model", openai_models)

query = st.text_input("Enter a news headline or claim:")

if st.button("Check"):
    if query:
        with st.spinner("Searching and analyzing..."):
            links = search_google(query)
            context = prepare_context(links)

            prompt = f"""
            I give you an information body from news and given a prompt you should detect if the prompt is a fake news or not briefly.
            I want to make decision accordingly.
            Here is the prompt:
            Prompt:
            {query}
            Information body:
            {context}
            """

            result = call_llm(prompt, model=model)

            st.subheader("Result:")
            st.write(result)
    else:
        st.warning("Please enter a query.")
