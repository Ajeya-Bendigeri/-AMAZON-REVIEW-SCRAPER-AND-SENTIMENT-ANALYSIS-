from textblob import TextBlob
from file2 import df

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  
df['Sentiment'] = df['Review Text'].apply(analyze_sentiment)

df.to_csv('iphone_reviews_with_sentiment.csv', index=False)