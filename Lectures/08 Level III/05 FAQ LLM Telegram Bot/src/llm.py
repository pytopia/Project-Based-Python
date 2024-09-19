import os

from loguru import logger
from openai import OpenAI

assert os.getenv("OPENAI_API_KEY") is not None, "OPENAI_API_KEY is not set"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_llm(prompt, model="gpt-4o-mini", system_prompt="You are a helpful assistant."):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
