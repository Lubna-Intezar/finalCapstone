
# Import necessary libraries
import pandas as pd
import spacy
from textblob import TextBlob



# Download the spaCy model (if not already downloaded)
nlp = spacy.load("en_core_web_sm")

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("amazon_product_reviews.csv", low_memory=False)

# Step 1: Preprocess the text data
def preprocess_text(text):
  
  #This function preprocesses the text data by removing stopwords and performing basic cleaning.
  
        # Lowercase the text
        text = text.lower()

        # Ensure spaCy model is applied to a string, not characters
        doc = nlp(text)  # Create a spaCy Doc object from the text

        # Remove stopwords using the Doc object
        tokens = [token.text for token in doc if not token.is_stop]

        # Remove punctuation and special characters (from the remaining tokens)
        clean_tokens = [token for token in tokens if token.isalnum() or token.isspace()]

        # Join the cleaned tokens back into a string
        return " ".join(clean_tokens)
        # Apply text preprocessing to the "review.text" column and create a new column
        data["cleaned_text"] = data["reviews.text"].apply(preprocess_text)

# Step 2: Define a function for sentiment analysis using TextBlob
def analyze_sentiment(text):
        """
            This function analyzes the sentiment of the text using TextBlob.
            """
        # Perform sentiment analysis using TextBlob
        sentiment = TextBlob(text).sentiment
        # Classify sentiment based on polarity score
        if sentiment.polarity > 0:
            return "positive"
        elif sentiment.polarity < 0:
            return "negative"
        else:
            return "neutral"

        # Apply sentiment analysis to the "cleaned_text" column and create a new column
        data["sentiment"] = data["cleaned_text"].apply(analyze_sentiment)

# Step 3: Print sample reviews with sentiment analysis
sample_reviews = ["This product is amazing!", "I am very disappointed with this product.", "It's okay, I guess."]
for review in sample_reviews:
        sentiment = analyze_sentiment(review)
        print(f"Review: {review} - Sentiment: {sentiment}")

