from openai import OpenAI
import os
import streamlit as st

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@st.cache_resource
def call_llm(prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    )
    return response.choices[0].message.content
