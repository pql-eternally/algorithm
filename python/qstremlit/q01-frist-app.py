import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df2 = np.random.randn(3, 4)
df3 = pd.DataFrame(df2, columns=['col %d' % i for i in range(4)])

st.write("Here's our first attempt at using data to create a table:")
st.write(df)
# st.dataframe(df2)
st.dataframe(df3.style.highlight_max(axis=0))
st.table(df3)
st.write("=" * 88)
st.line_chart(pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c']))
st.write("=" * 88)
st.map(pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']))
st.write("=" * 88)
x = st.slider('x')
st.write(x, 'squared is', x * x)
st.write("=" * 88)
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.write(chart_data)

st.write("=" * 88)
option = st.selectbox('Which number do you like best?', df['first column'])
st.write('You selected: ', option)
