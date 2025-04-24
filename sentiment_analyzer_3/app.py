import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

st.title("🧠 Sentiment Analysis App")
st.markdown("Enter your text below and get the sentiment (Positive, Negative, or Neutral).")

user_input = st.text_area("✍️ Enter your text:")

if st.button("Analyze Sentiment"):
    if user_input:
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "😊 Positive"
        elif polarity < 0:
            sentiment = "😞 Negative"
        else:
            sentiment = "😐 Neutral"

        st.success(f"Sentiment: **{sentiment}**")
    else:
        st.warning("Please enter some text to analyze.")
