import streamlit as st
import numpy as np
import pandas as pd
import json
import time
from streamlit_cookies_manager import EncryptedCookieManager
import os

df = pd.read_csv("../data/Anime_data.csv")

with open("../data/list_genre", "r") as fp:
    list_genre = json.load(fp)

with open("../data/list_type", "r") as fp:
    list_type = json.load(fp)

with open("../data/list_producer", "r") as fp:
    list_producer = json.load(fp)

with open("../data/list_studio", "r") as fp:
    list_studio = json.load(fp)



# This should be on top of your script
cookies = EncryptedCookieManager(
    prefix="ktosiek/streamlit-cookies-manager/",
    password=os.environ.get("COOKIES_PASSWORD", "lest go"),
)

#cookies['historical'] = "[]"
#cookies.save()

if not cookies.ready():
    st.stop()

try :
    historical = json.loads(cookies['historical'])
    st.write('cookies Find !')
    #st.title(historical)
except:
    st.write('cookies NOT find !')
    #cookies['historical'] = "[]"
    historical = []

def remove_cookie():
    question = ""
    cookies['historical'] = "[]"
    cookies.save()
    historical = []

def search(df,variable):
    if variable["Title"] != "":
        df = df[df['Title'].str.contains(title, case=False)]
    if variable["Genre"] != []:
        df = df.dropna()
        df = df[df['Genre'].str.contains('|'.join(Genre), case=False)]
    return df



st.title('perfect anime')

tab1, tab2 = st.tabs(["search", "tuto"])

with tab1:

    st.header('anime')
    with st.expander("search"):
        title = st.text_input(value="",label="Title")
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

    #with st.expander("advanced search"):
        #Rating =
        #Aired


    variable = {"Title":title,"Genre":Genre,"Description":Description,"Type":type, "producer":producer, "Studio":Studio}
    if st.button('Say hello'):
        st.write('Why hello there')

    if st.button('manger les cookies 🍪' ):
        remove_cookie()
    else:
        pass

    df = search(df,variable)
    st.dataframe(df)



with tab2:
    st.header('documentation')
    recherche = st.text_input(value="", label="recherche")


























