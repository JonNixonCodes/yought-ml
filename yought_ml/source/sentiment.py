# sentiment.py

# %% Import external libraries
from textblob import TextBlob

# %% Define functions
def extract_sentiment(text):
    return TextBlob(text).sentiment.polarity

def extract_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def extract_sentiment_tokens(text):
    blob = TextBlob(text)
    sentiment_tokens = [a[:2] for a in blob.sentiment_assessments.assessments]
    # Extract token position
    return sentiment_tokens

def extract_subjectivity_tokens(text):
    blob = TextBlob(text)
    subjectivity_tokens = [(a[0],a[2]) for a in blob.sentiment_assessments.assessments]
    # Extract token position
    return subjectivity_tokens    
