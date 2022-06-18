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
    return df

def buying_recovery(endDate,setRange):
    res = call_api(endDate,setRange)
    
    fig1_data = px.bar(res,x=res['Quote'],y=res['%Change '+res['End Month'].iloc[0]])._data
    fig2_data = px.bar(res,x=res['Quote'],y=res['%Change '+res['Begin Month'].iloc[0]])._data

    fig1_data[0]['marker']['color'] = 'rgba(0,128,0, 0.6)'
    #fig1_data[1]['marker']['color'] = 'rgba(0,128,0, 0.6)'

    fig2_data[0]['marker']['color'] = 'rgba(0,0,255, 0.6)'
    #fig2_data[1]['marker']['color'] = 'rgba(0,0,255, 0.6)'

    dat = fig1_data+fig2_data
    fig = go.Figure(dat)

    fig3 = go.Figure(fig._data)
    fig.update_layout(barmode='relative', title_text='Relative Barmode')
    fig3.show()
    

# Unit Test
endDate = '2022-06-17'
setRange = 'SET50'
print(buying_recovery(endDate,setRange))