import streamlit as st
import plotly_express as px
import pandas as pd
import yfinance as yf
from datetime import datetime

def above_ema():
    #Tile
    st.title("SET100: Above EMA")
    
    # Set current Date
    currentDate = datetime.today().strftime('%Y-%m-%d')

    #EMA Length
    ema_length = st.selectbox('EMA Length',('EMA 5','EMA 20','EMA 60'))

    #Date Select
    date = st.date_input("Date", value=pd.to_datetime(currentDate, format="%Y-%m-%d"))