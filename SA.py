import nltk
nltk.download('vader_lexicon')
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the vader_lexicon resource if not already downloaded
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Streamlit app title
st.title("Sentiment Analysis App")

# Input text area for user input
user_input = st.text_area("Enter text to analyze:")

# Sentiment analysis function
def analyze_sentiment(text):
    sentiment_score = sid.polarity_scores(text)
    return sentiment_score

# Perform sentiment analysis when user clicks the button
if st.button("Analyze"):
    # Check if user input is empty
    if user_input:
        sentiment_score = analyze_sentiment(user_input)
        st.write("Sentiment Scores:")
        st.write(sentiment_score)
        # Determine sentiment based on compound score
        if sentiment_score["compound"] > 0.05:
            st.write("Overall Sentiment: Positive")
        elif sentiment_score["compound"] < -0.05:
            st.write("Overall Sentiment: Negative")
        else:
            st.write("Overall Sentiment: Neutral")
    else:
        st.warning("Please enter some text to analyze.")
