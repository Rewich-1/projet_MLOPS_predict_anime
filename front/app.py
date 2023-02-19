import streamlit as st
import numpy as np
import pandas as pd
import json
import time
from streamlit_cookies_manager import EncryptedCookieManager
import os

from search import page_search
from predict import page_predict

st.title('perfect anime')

tab1, tab2 , tab3= st.tabs(["dataframe","predict", "tuto"])

with tab1:
    page_search()

with tab2:
    page_predict()

with tab3:
    st.header('documentation')
