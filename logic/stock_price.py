import streamlit as st
import plotly_express as px
import pandas as pd
import yfinance as yf
from datetime import datetime

def stock_price_visualize():
    #Tile
    st.title("Stock Price Trend")
        
    #STOCK_LIST
    quote = st.text_input("Stock Quote", placeholder= 'Stock Quote',value = "PTT")+'.BK'

    #Set current Date
    start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01", format="%Y-%m-%d"))
    end_date = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))

    #Get data
    quoteData = yf.Ticker(quote)

    #Logic
    stock_price = quoteData.history(period='1d', start = start_date, end = end_date)

    st.line_chart(stock_price.Close)
    st.line_chart(stock_price.Volume)