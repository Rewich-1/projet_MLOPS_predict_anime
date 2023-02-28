import streamlit as st
import numpy as np
import pandas as pd
import json
import time
from streamlit_cookies_manager import EncryptedCookieManager
import os
import random
import requests
import math
from sentence_transformers import SentenceTransformer
sbert = SentenceTransformer ('distilbert-base-nli-mean-tokens')

with open("./data/list_genre", "r") as fp:
    list_genre = json.load(fp)
with open("./data/list_type", "r") as fp:
    list_type = json.load(fp)

with open("./data/list_producer", "r") as fp:
    list_producer = json.load(fp)

with open("./data/list_studio", "r") as fp:
    list_studio = json.load(fp)

def preprocess(variable):
    global list_genre, list_type, list_producer, list_studio
    def dummies_normalized(col,listt):
        l = []
        for g in sorted(listt):
            if g in variable[col]:
                l.append(1)
            else:
                l.append(0)
        total = sum(l) if sum(l) != 0 else 1
        return [x/math.sqrt(total) for x in l]
    
    variable['Genre'] = [dummies_normalized('Genre',list_genre)]
    variable['Producer'] = [dummies_normalized('Producer',list_producer)]
    variable['Studio'] = [dummies_normalized('Studio',list_studio)]
    variable['Type'] = [dummies_normalized('Type',list_type)]
    
    r = pd.DataFrame(variable)

    r['Title'] = sbert.encode(r['Title'].values , show_progress_bar =True).tolist()  
    r['Synopsis'] = sbert.encode(r['Synopsis'].values , show_progress_bar =True).tolist()

    t = pd.DataFrame(r['Title'].tolist())
    g = pd.DataFrame(r['Genre'].tolist()) 
    syn = pd.DataFrame(r['Synopsis'].tolist())
    ty = pd.DataFrame(r['Type'].tolist())  
    p = pd.DataFrame(r['Producer'].tolist())
    s = pd.DataFrame(r['Studio'].tolist())


    df_pred = pd.concat([t,g,syn,ty,p,s], axis=1)
    r = df_pred.iloc[0].values.tolist()

    return r


def requests_api(variable):
    URL = 'http://back:5000/predict_rating'
    rating = requests.post(URL, json.dumps(variable))
    print("Prediction = " + str({rating.text}))
    rating = float(rating.text[1:-1])
    return rating


def page_predict():

    st.warning('We are experiencing exceptionally high demand. Please hang tight as we work on scaling our systems.', icon="⚠️")

    df = pd.read_csv("./data/Anime_data.csv")

    with open("./data/list_genre", "r") as fp:
        list_genre = json.load(fp)

    with open("./data/list_type", "r") as fp:
        list_type = json.load(fp)

    with open("./data/list_producer", "r") as fp:
        list_producer = json.load(fp)

    with open("./data/list_studio", "r") as fp:
        list_studio = json.load(fp)

    with open("./data/site_to_api", "r") as fp:
        site_to_api = json.load(fp)
    site_to_api = str(site_to_api)
    site_to_api = site_to_api.replace(" ", "").replace('"', "").replace("[", "").replace("]", "").replace("'", "")
    site_to_api = list(site_to_api.split(","))


    st.header('predict rating of your anime')
    with st.expander("search"):
        predict_title = st.text_input(value="", label="predict_Title")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            predict_Genre = st.multiselect(label="predict_Genre", options=list_genre)
        with col2:
            predict_type = st.selectbox(label="predict_Type", options=list_type)
        with col3:
            predict_producer = st.multiselect(label="predict_producer", options=list_producer)
        with col4:
            predict_Studio = st.multiselect(label="predict_studio", options=list_studio)
        predict_Description = st.text_area(label="predict_Description")

    #with st.spinner('Wait for it...'):
    #   time.sleep(2)
    #   rating_predict = requests_api(variable)


    #st.header('result')

    #st.write(variable)
    #st.write(site_to_api)

    # list_api = [0] * len(site_to_api)

    # for key, value  in variable.items():
    #     #st.write(value)
    #     for i in value:
    #         if i in site_to_api:
    #             st.write(i)
    #             st.write(site_to_api.index(i))
    #             list_api[site_to_api.index(i)] = 1

    # rating_predict = requests_api(list_api)

    #GETTING THE ROW TO PREDICT AND MAKING IT INTO THE BEST FORMAT FOR THE MODEL

    variable = {"Title": [predict_title], "Genre": [predict_Genre], "Synopsis": [predict_Description], "Type": [predict_type], "Producer": [predict_producer],"Studio": [predict_Studio]}

    row_to_predict = preprocess(variable)
    #print(row_to_predict)
    #print(len(row_to_predict))
    print(row_to_predict)
    rating_predict = requests_api(row_to_predict)
    #st.write(rating_predict)

    if rating_predict == 0:
        st.error('api not work', icon="🚨")
    else:

        st.header('result')

        my_bar = st.progress(1)

        time.sleep(1)
        my_bar.progress(0.8)

        time.sleep(1)
        my_bar.progress(0.2)

        time.sleep(1)
        my_bar.progress(rating_predict/10)

        color = {
           "red": 0,
           "green": 0,
            "blue": 60,
        }

        if rating_predict < 50:
            color["red"] = 255 - int(rating_predict * 2)
            color["green"] = int(255-50+rating_predict * 2)
        else:

            st.header('result')

            my_bar = st.progress(1)

        st.balloons()
        with col1:
            st.markdown("<h1 style='text-align: center'>💯</h1>", unsafe_allow_html=True)
        with col2:
           st.header('your anime has a rating of:\n')
           st.title(rating_predict)
        with col3:
           st.markdown("<h1 style='text-align: center'>💯</h1>", unsafe_allow_html=True)
