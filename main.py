from ssl import get_protocol_name
from matplotlib.pyplot import text
from more_itertools import map_except
import uvicorn
from fastapi import FastAPI
import joblib
from utils import get_prior_n_links
import pandas as pd

import tweet_scraper
from pydantic import BaseModel

from tweet_scraper import Import_tweet_sentiment
tw_obj=Import_tweet_sentiment()

import os
from os.path import dirname, join, realpath

from train_app import tokenize

port = 8000

app = FastAPI()

with open(
    join(dirname(realpath(__file__)), "classifier_ea.pkl"), "rb"
) as f:
    model = joblib.load(f)

df = pd.read_csv('data/figure_eight_data.csv')


@app.get('/')
def index():

    return {'message': "This is the main page.. See you in a bit!"}


@app.get('/predict')
def predict(data: str):

    query = data

    print(query)

    all_tweets=tw_obj.get_hashtag(query)

    target_text = all_tweets

    print(target_text)

    query2=all_tweets[0]

    results_list = []
    priority_list = []
    maps_list = []
    
    classification_labels = model.predict([query2])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))
    for category, classification in classification_results.items():
        if classification==1:
            results_list.append(category)
            priority,maps=get_prior_n_links(category)
            priority_list.append(priority)
            maps_list.append(maps)


    print(results_list)



    return {
        'classification_results':results_list, 'priority':priority_list,'maps':maps_list
    }


@app.get('/predict_wi')
def predict_wi(data: str):

    query = data

    print(query)
    results_list = []
    priority_list = []
    maps_list = []
    
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))
    for category, classification in classification_results.items():
        if classification==1:
            results_list.append(category)
            priority,maps=get_prior_n_links(category)
            priority_list.append(priority)
            maps_list.append(maps)


    print(results_list)



    return {
        'classification_results':results_list, 'priority':priority_list,'maps':maps_list
    }

if __name__ == '__main__':

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)