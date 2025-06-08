import streamlit as st
from scraper import get_reviews
from summarizer import summarize_reviews

st.set_page_config(page_title="ReviewPulse", layout="centered")
st.title("📱 ReviewPulse - Customer Review Summarizer")

app_id = st.text_input("Enter Google Play App ID (e.g., com.duolingo)")

if st.button("Fetch & Summarize"):
    with st.spinner("Collecting reviews..."):
        reviews = get_reviews(app_id)
        st.success(f"Fetched {len(reviews)} reviews")

    with st.spinner("Summarizing with AI..."):
        summary = summarize_reviews(reviews)
        st.subheader("🧠 AI Summary")
        st.write(summary)
