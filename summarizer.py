import streamlit as st
import os
from openai import OpenAI, RateLimitError

def load_api_key():
    if "OPENAI_API_KEY" in st.secrets:
        return st.secrets["OPENAI_API_KEY"]
    elif os.path.exists("openai_key.txt"):
        return open("openai_key.txt").read().strip()
    else:
        raise ValueError("OpenAI API key not found.")

client = OpenAI(api_key=load_api_key())

def summarize_reviews(reviews_list):
    joined_reviews = "\n\n".join(reviews_list[:50])
    prompt = f"""
    Summarize the following customer reviews into:
    1. Bugs
    2. UX issues
    3. Feature requests
    4. Positive feedback

    Reviews:\n{joined_reviews}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except RateLimitError:
        return "⚠️ Rate limit exceeded. Please wait and try again shortly."
