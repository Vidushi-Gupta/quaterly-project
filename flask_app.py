import json
import plotly
import pandas as pd
import numpy as np

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import joblib
import tweet_scraper

from flask import Flask
from flask import render_template, request
from plotly.graph_objs import Bar




from tweet_scraper import Import_tweet_sentiment
tw_obj=Import_tweet_sentiment()
from nltk.tokenize import word_tokenize

app = Flask(__name__)


def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

df = pd.read_csv('data/figure_eight_data.csv')

# load model




@app.route('/')
@app.route('/index')
def index():
    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)

    # Show distribution of different category
    category = list(df.columns[4:])
    category_counts = []
    for column_name in category:
        category_counts.append(np.sum(df[column_name]))

    # extract data exclude related
    categories = df.iloc[:, 4:]
    categories_mean = categories.mean().sort_values(ascending=False)[1:11]
    categories_names = list(categories_mean.index)

    # render web page with plotly graphs
    return render_template('master.html')


# web page that handles user query and displays model results
@app.route('/go')
def go():

    model = joblib.load("classifier_ea.pkl")
    # save user input in query
    query = request.args.get('query', '')

    all_tweets=tw_obj.get_hashtag(query)

    target_text = all_tweets

    print(target_text)
    query2=all_tweets[0]

    # use model to predict classification for query
    classification_labels = model.predict([query2])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file.
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results,tweet_collect=all_tweets[0]
    )


if __name__ == '__main__':
    app.run(debug=True)
