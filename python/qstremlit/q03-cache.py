import streamlit as st
import time
import pandas as pd
import numpy as np
import requests


@st.cache_data
def long_running_function(a, b):
    time.sleep(2)
    return a + b


# res = long_running_function(1, 2)
# st.write(res)


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    return pd.read_csv(url)


df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)


@st.cache_data
def transform(df):
    df = df.filter(items=['one', 'three'])
    df = df.apply(np.sum, axis=0)
    return df


@st.cache_data
def api_call():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return response.json()


st.dataframe(transform(df))
st.write(api_call())
st.button("Rerun")
