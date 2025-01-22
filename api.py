
from sentiment_analysis import analyze_sentiment

from flask import Flask, render_template, request, jsonify
import pandas as pd
from textblob import TextBlob
import mysql.connector

app = Flask(__name__)


reviews_df = pd.read_csv('iphone_reviews_with_sentiment.csv')


app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'scrapping'

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

# def analyze_sentiment(review_text):
#     analysis = TextBlob(review_text)
#     if analysis.sentiment.polarity > 0:
#         return 'positive'
#     elif analysis.sentiment.polarity < 0:
#         return 'negative'
#     else:
#         return 'neutral'

@app.route('/', methods=['GET'])
def display():
    return render_template('display.html')

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    review = request.form.get('review')
    sentiment = analyze_sentiment(review)

    cursor = mysql.cursor()
    sql = "INSERT INTO reviews (review_text, sentiment) VALUES (%s, %s)"
    val = (review, sentiment)
    cursor.execute(sql, val)
    mysql.commit()

    return render_template('sentiment.html', sentiment=sentiment, review=review)

@app.route('/reviews', methods=['GET'])
def get_reviews():
    color = request.args.get('color')
    storage_size = request.args.get('storage_size')
    rating = request.args.get('rating')

    try:
        rating = float(rating) if rating is not None else None
    except ValueError:
        return jsonify({'error': 'Invalid rating value'}), 400

    conditions = []
    if color:
        conditions.append(reviews_df['Colour'] == color)
    if storage_size:
        conditions.append(reviews_df['Style Name'] == storage_size)
    if rating is not None:
        conditions.append(reviews_df['Rating'] == rating)

    filtered_reviews = reviews_df[pd.concat(conditions, axis=1).all(axis=1)] if conditions else reviews_df

    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM reviews")
    reviews_from_db = cursor.fetchall()



    return jsonify(filtered_reviews.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)