import openai
import streamlit as st  # Required for accessing secrets

# Load the API key from Streamlit secrets (ideal for Streamlit Cloud)
def load_api_key():
    return st.secrets["OPENAI_API_KEY"]

openai.api_key = load_api_key()

def summarize_reviews(reviews_list):
    joined_reviews = "\n\n".join(reviews_list[:50])  # Limit for brevity
    prompt = f"""
    Summarize the following customer reviews into:
    1. Bugs
    2. UX issues
    3. Feature requests
    4. Positive feedback

    Reviews:\n{joined_reviews}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response['choices'][0]['message']['content']
    return summary


    return response.choices[0].message.content
