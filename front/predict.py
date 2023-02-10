import streamlit as st
import numpy as np
import pandas as pd
import json
import time
from streamlit_cookies_manager import EncryptedCookieManager
import os
import random
import requests


def requests_api(variable):
    #URL = 'http://127.0.0.1:5000/classify'
    #result = requests.post(URL, json.dumps(variable))
    #print("Prediction = " + str({result.text}))
    rating = random.randint(20, 80)
    return rating


def page_predict():
    df = pd.read_csv("../data/Anime_data.csv")

    with open("../data/list_genre", "r") as fp:
        list_genre = json.load(fp)

    with open("../data/list_type", "r") as fp:
        list_type = json.load(fp)

    with open("../data/list_producer", "r") as fp:
        list_producer = json.load(fp)

    with open("../data/list_studio", "r") as fp:
        list_studio = json.load(fp)

    st.header('predict rating of your anime')
    with st.expander("search"):
        predict_title = st.text_input(value="", label="predict_Title")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            predict_Genre = st.multiselect(label="predict_Genre", options=list_genre)
        with col2:
            predict_type = st.multiselect(label="predict_Type", options=list_type)
        with col3:
            predict_producer = st.multiselect(label="predict_producer", options=list_producer)
        with col4:
            predict_Studio = st.multiselect(label="predict_studio", options=list_studio)
        predict_Description = st.text_area(label="predict_Description")

    variable = {"Title": predict_title, "Genre": predict_Genre, "Description": predict_Description, "Type": type, "producer": predict_producer,
                "Studio": predict_Studio}

    with st.spinner('Wait for it...'):
        time.sleep(2)
        rating_predict = requests_api(variable)


    st.header('result')


    my_bar = st.progress(50)

    time.sleep(1)
    my_bar.progress(rating_predict+20)

    time.sleep(1)
    my_bar.progress(rating_predict - 20)

    time.sleep(1)
    my_bar.progress(rating_predict)

    color = {
        "red": 0,
        "green": 0,
        "blue": 60,
    }

    if rating_predict < 50:
        color["red"] = 255 - int(rating_predict * 2)
        color["green"] = int(255-50+rating_predict * 2)
    else:
        color["red"] = 255 - int(rating_predict * 2.55)
        color["green"] = int(rating_predict * 2.55)

    st.markdown("""
               <style>
               .stProgress .st-ep {
                   background-color: rgb("""+str(color['red'])+""", """+str(color['green'])+""", """+str(color['blue'])+""")
               }
               </style>
               """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    st.balloons()
    with col1:
        st.markdown("<h1 style='text-align: center'>💯</h1>", unsafe_allow_html=True)
    with col2:
        st.header('your anime have rating of  :'+ str(rating_predict/10))
    with col3:
        st.markdown("<h1 style='text-align: center'>💯</h1>", unsafe_allow_html=True)


    #st.dataframe(df)