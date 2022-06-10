import streamlit as st
import pandas as pd
import requests
from datetime import datetime

def call_api(quote,startDate,endDate):
    response = requests.get('http://127.0.0.1:8000/stockprice',params={'quote': quote,'startDate': startDate,'endDate': endDate})
    result = response.text
    df = pd.read_json(result, orient ='index')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    st.dataframe(df)
    return df

def export_data():
    #Tile
    st.header("Export Data")
    
    with st.form(key='searchform'):
        nav1,nav2,nav3,nav4 = st.columns([4,3,2,1])
        
        with nav1:
            #STOCK_LIST
            quote = st.text_input("Stock Quote", placeholder= 'Stock Quote',value = "PTT")
        with nav2:
            #Set current Date
            startDate = st.date_input("Start Date", value=pd.to_datetime("2020-01-01", format="%Y-%m-%d"))
        with nav3:    
            endDate = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
        #button1
        col1,col2 = st.columns(2)
        with col1:
            submit_search = st.form_submit_button(label='Search')
    
    if submit_search:
        df = call_api(quote,startDate,endDate)
        csv = df.to_csv().encode('utf-8')
        st.download_button(label='Export to CSV',data=csv,file_name=quote+'_Data.csv')
    if not submit_search:
        st.download_button(label='Export to CSV',data='',file_name=quote+'_Data.csv',disabled=True)   
