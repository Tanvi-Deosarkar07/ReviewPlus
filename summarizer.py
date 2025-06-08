import openai

def load_api_key():
    with open("openai_key.txt") as f:
        return f.read().strip()

openai.api_key = load_api_key()

def summarize_reviews(reviews_list):
    joined_reviews = "\n\n".join(reviews_list[:50])  # Keep it short for prompt
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

    return response.choices[0].message.content
