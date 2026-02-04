import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("data/customer reviews.csv")
df_top100_books = pd.read_csv("data/Top-100 Trending Books.csv")

st.write("## Customer Reviews")
st.dataframe(df_reviews)


price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

price_range = st.sidebar.slider(
    "Price Range",
    min_value=price_min,
    max_value=price_max,
    value=(price_min, price_max),
)

df_books = df_top100_books[
    (df_top100_books["book price"] >= price_range[0])
    & (df_top100_books["book price"] <= price_range[1])
]

st.write("## Top 100 Trending Books")
st.dataframe(df_books)

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
