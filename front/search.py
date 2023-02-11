import streamlit as st
import numpy as np
import pandas as pd
import json
import time
from streamlit_cookies_manager import EncryptedCookieManager
import os



def search(df,variable):
    if variable["Title"] != "":
        df = df[df['Title'].str.contains(variable["Title"], case=False)]
    if variable["Genre"] != []:
        df = df.dropna()
        df = df[df['Genre'].str.contains('|'.join(variable["Genre"]), case=False)]
    return df


def page_search():
    df = pd.read_csv("../data/Anime_data.csv")

    with open("../data/list_genre", "r") as fp:
        list_genre = json.load(fp)

    with open("../data/list_type", "r") as fp:
        list_type = json.load(fp)

    with open("../data/list_producer", "r") as fp:
        list_producer = json.load(fp)

    with open("../data/list_studio", "r") as fp:
        list_studio = json.load(fp)

    st.header('anime')
    with st.expander("search"):
        title = st.text_input(value="", label="Title")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            Genre = st.multiselect(label="Genre", options=list_genre)
        with col2:
            type = st.multiselect(label="Type", options=list_type)
        with col3:
            producer = st.multiselect(label="producer", options=list_producer)
        with col4:
            Studio = st.multiselect(label="studio", options=list_studio)
        Description = st.text_area(label="Description")

    variable = {"Title": title, "Genre": Genre, "Description": Description, "Type": type, "producer": producer,
                "Studio": Studio}

    df = search(df, variable)
    st.dataframe(df)