import streamlit as st
import plotly_express as px
import pandas as pd
from datetime import date

def market_anomaly():
    #Tile
    st.title("Market Anomaly")
    
    today_date = date.today()
    current_year = today_date.year+1
    with st.form(key='visualizeform'):    
        #STOCK_LIST
        quote = st.text_input("Stock Quote", placeholder= 'Stock Quote',value = "SET")

        #Set current Date
        beginYear = st.selectbox('Begin Year', range(1975,current_year))
        endYear = st.selectbox('End Year', range(1975,current_year))
        period = st.selectbox('Period',('Week','2 Weeks','Month'))
        submit_visualize = st.form_submit_button(label='Visualize')
    if submit_visualize:
        if beginYear > endYear:
            st.error('The Begin Year must be before End Year!')
            

