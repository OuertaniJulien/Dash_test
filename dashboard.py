import pandas as pd
import streamlit as st

import plotly.express as px


st.set_page_config(page_title="Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")
st.sidebar.header("Header")


dt_week= pd.read_csv("export.csv") 
# dt_week.columns
dt_week = dt_week.rename(columns={'écart d\'inventaire Total':'ecart','Pertes Total':'Pertes'})
# dt_week.columns

head = dt_week[['Période du', 'Produit', 'Pertes', 'ecart']].head(5)
tail = dt_week[['Période du', 'Produit', 'Pertes', 'ecart']].tail(5)

head
chart = px.bar(
    head,
    x="Produit",
    y="Pertes",
    orientation="v",
    title="title",
    template="plotly_white"
 )

st.plotly_chart(chart)

tail
chart2 = px.bar(
    tail,
    x="Produit",
    y="ecart",
    orientation="v",
    title="title",
    template="plotly_white"
 )

st.plotly_chart(chart2)