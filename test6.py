from urllib import response
from pyrfc3339 import generate
import streamlit as st
from streamlit_option_menu import option_menu
import plotly_express as px
import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
from datetime import datetime
import requests

def call_api(endDate,setRange):
    response = requests.get('http://127.0.0.1:8000/buyingRecovery',params={'endDate': endDate,'setRange': setRange})
    result = response.text
    df = pd.read_json(result, orient ='index')
    df = pd.DataFrame(df)
    df.reset_index(inplace=True)
    df.rename(columns = {'index':'Quote'}, inplace = True)
    df1 = df[['Quote','Selected Date','Begin Month','%Change '+df['Begin Month'].iloc[0]]]
    df1.rename(columns = {'Begin Month':'Month','%Change '+df['Begin Month'].iloc[0]:'%Change'}, inplace = True)
    df2 = df[['Quote','Selected Date','End Month','%Change '+df['End Month'].iloc[0]]]
    df2.rename(columns = {'End Month':'Month','%Change '+df['End Month'].iloc[0]:'%Change'}, inplace = True)
    df3 = pd.concat([df1,df2])
    df3.reset_index(inplace=True)
    return df3

def buying_recovery(endDate,setRange):
    res = call_api(endDate,setRange)
    
# Unit Test
endDate = '2022-06-17'
setRange = 'SET50'

# print(generate_plot_data(endDate,setRange))
print(call_api(endDate,setRange))