import streamlit as st
import plotly_express as px
import pandas as pd
import yfinance as yf
from datetime import datetime
import requests

def call_api(quote,startDate,endDate):
    response = requests.get('http://127.0.0.1:8000/stockprice',params={'quote': quote,'startDate': startDate,'endDate': endDate})
    result = response.text
    df = pd.read_json(result, orient ='index')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    st.dataframe(df)
    return df

def set100_change():
    #Tile
    st.title("SET100: Daily Change(%)")
    
    with st.form(key='visualizeform'):
        #Date Select
        startDate = st.date_input("Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
        endDate = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
        submit_visualize = st.form_submit_button(label='Visualize')
    
        if submit_visualize:
            result = call_api('^SET.BK',startDate,endDate)        